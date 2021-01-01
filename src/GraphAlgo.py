from builtins import list
from collections import deque
from typing import List
from queue import PriorityQueue
import json


import GraphInterface
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: GraphInterface = None):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        with open(file_name) as json_file:
            data = json.load(json_file)
        nodes = data["Nodes"]
        edges = data["Edges"]
        graph = DiGraph()

        if nodes is not None and edges is not None:
            for node_element in nodes:
                if node_element.get("id") is not None:
                    key = node_element.get("id")
                    if node_element.get("pos") is not None:
                        pos = node_element.get("pos")
                        graph.add_node(key, pos)
                    else:
                        graph.add_node(key=key)
                else:
                    return False
            for edge_element in edges:
                if edge_element.get("src") is not None and edge_element.get("w") is not None and edge_element.get("dest") is not None:
                    src = edge_element.get("src")
                    weight = edge_element.get("w")
                    dest = edge_element.get("dest")
                    graph.add_edge(src, dest, weight);
                else:
                    return False
            self.graph = graph
        else:
            return False
        return True

    def save_to_json(self, file_name: str) -> bool:
        nodes_list = []
        edges_list = []
        json_dict = dict()
        all_nodes = self.graph.get_all_v().values()
        for node in all_nodes:
            curr_node = dict()
            pos_tup = node.get_pos()
            pos_str = ""
            if pos_tup is None:
                pos_str = "-1,-1,-1"
            else:
                for i in pos_tup:
                    pos_str += str(i)
                    pos_str += ","
                pos_str = pos_str[:-1]
            curr_node["pos"] = pos_str
            curr_node["id"] = node.get_key()
            nodes_list.append(curr_node)

            all_edges_from_node = self.graph.all_out_edges_of_node(node.get_key())
            for edge in all_edges_from_node.keys():
                curr_edge = dict()
                curr_edge["src"] = node.get_key()
                curr_edge["w"] = all_edges_from_node.get(edge)
                curr_edge["dest"] = edge
                edges_list.append(curr_edge)
        json_dict["Edges"] = edges_list
        json_dict["Nodes"] = nodes_list
        with open(file_name, 'w') as file:
            json.dump(json_dict, file)
            return True


    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if self.graph is None:
            return [float('inf'), []]
        prev = self.__dijkstra(id1, id2)
        path = self.__reconstruct_path(prev, id1, id2)
        if path is None:
            return (float('inf'), [])
        else:
            nodes = self.graph.get_all_v()
            ans = (nodes[id2].get_tag(), path)
            return ans

    def __dijkstra(self, src: int, dest: int):
        pq = PriorityQueue()
        dist = float('inf')
        visited = set()
        prev = dict()
        nodes = self.graph.get_all_v()
        nodes[src].set_tag(0)
        pq.put((nodes[src].get_tag(), src))
        while len(pq.queue) != 0:
            curr_key = pq.get(0)[1]
            curr = nodes[curr_key]
            if curr_key not in visited and curr_key != dest:
                visited.add(curr_key)
                curr_ni = nodes[curr_key].get_edges_from_node().keys()
                for ni_key in curr_ni:
                    ni = nodes[ni_key]
                    if ni_key not in visited:
                        ni_dist_from_src = curr.get_tag() + curr.get_edge_weight(ni_key)
                        if ni_dist_from_src < dist:
                            if ni_key == dest:
                                dist = ni_dist_from_src
                        if prev.get(ni_key) is None:
                            ni.set_tag(ni_dist_from_src)
                            prev[ni_key] = curr_key
                        elif ni_dist_from_src < ni.get_tag():
                            ni.set_tag(ni_dist_from_src)
                            prev[ni_key] = curr_key
                        pq.put((ni.get_tag(), ni_key))
        return prev

    def __reconstruct_path(self, prev: dict, src: int, dest: int):
        path_temp = [dest]
        i = dest
        while prev.get(i) is not None:
            path_temp.append(prev.get(i))
            i = prev.get(i)

        if len(path_temp) != 0 and path_temp[len(path_temp)-1] is src:
            path_temp.reverse()
            return path_temp
        else:
            return None

    def connected_component(self, id1: int) -> list:
        flag = False
        reversed = DiGraph()
        nodes = self.graph.get_all_v()
        if len(nodes) == 0:
            return []
        q = deque()
        q.append(id1)
        connected = {id1: True}
        connections_list = [id1]
        reversed.add_node(id1)
        while len(q) != 0:
            curr = q.popleft()
            curr_edges = self.graph.all_out_edges_of_node(curr)
            for curr_ni in curr_edges.keys():
                reversed.add_node(curr_ni)
                reversed.add_edge(curr_ni, curr, curr_edges.get(curr_ni))
                if connected.get(curr_ni) is None:
                    q.append(curr_ni)
                    connected[curr_ni] = True
                    connections_list.append(curr_ni)
        q.append(id1)
        r_connected = {id1: True}
        r_connections_list = [id1]
        while len(q) != 0:
            curr = q.popleft()
            curr_edges = reversed.all_out_edges_of_node(curr)
            for curr_ni in curr_edges.keys():
                if r_connected.get(curr_ni) is None:
                    q.append(curr_ni)
                    r_connected[curr_ni] = True
                    r_connections_list.append(curr_ni)
        return list(set(connections_list) & set(r_connections_list))








    def connected_components(self) -> List[list]:
        if self.graph is None:
            return []
        nodes = self.graph.get_all_v()
        keys = nodes.keys()
        ans = []
        connected = []
        for key in keys:
            if key not in connected:
                key_connected = self.connected_component(key)
                connected.extend(key_connected)
                ans.append(key_connected)
        return ans

    def plot_graph(self) -> None:
        pass



