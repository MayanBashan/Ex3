from GraphInterface import GraphInterface
from node_data import NodeData


class DiGraph(GraphInterface):

    def __init__(self):
        self.nodes = {}
        self.mc = 0
        self.edge_size = 0

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return self.edge_size

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.nodes.get(id1).get_edges_to_node()

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.nodes.get(id1).get_edges_from_node()

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 == id2:
            return False
        elif (id1 not in self.nodes.keys()) or (id2 not in self.nodes.keys()):
            return False
        elif id2 in self.all_out_edges_of_node(id1).keys():
            return False
        else:
            self.nodes.get(id1).add_edge_from_node(id2, weight)
            self.nodes.get(id2).add_edge_to_node(id1, weight)
            self.mc += 1
            self.edge_size += 1
            return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes.keys():
            return False
        else:
            new_node = NodeData(key=node_id)
            self.nodes[node_id] = new_node
            return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.nodes.keys():
            return False
        else:
            neighbors_to_node = self.all_in_edges_of_node(node_id).keys()
            for ni_key in neighbors_to_node:
                self.remove_edge(ni_key, node_id)

            neighbors_from_node = self.all_out_edges_of_node(node_id).keys()
            for ni_key in neighbors_from_node:
                self.remove_edge(node_id, ni_key)

            del self.nodes[node_id]
            self.mc += 1
            return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 == node_id2:
            return False
        elif node_id1 not in self.nodes.keys() or node_id2 not in self.nodes.keys():
            return False
        elif node_id2 not in self.all_out_edges_of_node(node_id1).keys():
            return False
        else:
            print(self.nodes.get(node_id1).get_edges_from_node())
            del self.nodes.get(node_id1).get_edges_from_node()[node_id2]
            del self.nodes.get(node_id2).get_edges_to_node()[node_id1]
            print(self.nodes.get(node_id1).get_edges_from_node())
            self.edge_size -= 1
            self.mc += 1
            return True
