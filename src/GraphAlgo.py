from typing import List
from queue import PriorityQueue
import json


import GraphInterface
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from node_data import NodeData


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: GraphInterface = None):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        with open(file_name, 'r') as file:
            data = json.load(file)
            print(data)

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        prev = self.__Dijkstra(id1, id2)
        path = self.__reconstructPath(prev, id1, id2)
        if path is None:
            return [float('inf'), []]
        else:
            nodes = self.graph.get_all_v()
            ans = [nodes[id2].get_tag(), path]
            return ans

    def __Dijkstra(self, src: int, dest: int):
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

    def __reconstructPath(self, prev: dict, src: int, dest: int):
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
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass


if __name__ == '__main__':
    string = "data\\A5"
    gg = DiGraph()
    g = GraphAlgo(gg)
    g.load_from_json(string)


