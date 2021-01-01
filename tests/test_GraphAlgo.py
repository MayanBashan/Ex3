from unittest import TestCase

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):
    """Test Class for DiGraph
    List of all the test in this Test class:
    - test_get_graph - checks if the simple method get_graph returns the algo_graph graph
    - test_load_from_json -
    - test_save_to_json -
    - test_shortest_path - checks if the shortest_path method returns the path from src to dest with the smallest dist between them
    - test_connected_component -
    - test_connected_components -
    - test_plot_graph -
    """

    def test_get_graph(self):
        graph = DiGraph()
        for i in range(0,5):
            graph.add_node(i)
        graph_algo = GraphAlgo(graph)
        self.assertEqual(graph_algo.get_graph(), graph)


    def test_load_from_json(self):
        self.fail()

    def test_save_to_json(self):
        self.fail()

    def test_shortest_path(self):
        graph = DiGraph()
        for i in range(0,5):
            graph.add_node(i)
        graph.add_edge(0,1,10)
        graph.add_edge(0,2,3)
        graph.add_edge(2,3,4)
        graph.add_edge(3,1,1)
        graph_algo = GraphAlgo(graph)
        comp_path = [0, 2, 3, 1]
        expected = [8, comp_path]
        self.assertEqual(graph_algo.shortest_path(0,1), expected)
        expected = [0, [0]]
        self.assertEqual(graph_algo.shortest_path(0,0), expected)
        expected = [float('inf'), []]
        self.assertEqual(graph_algo.shortest_path(2,4), expected)
        self.assertEqual(graph_algo.shortest_path(1,0), expected)

    def test_connected_component(self):
        self.fail()

    def test_connected_components(self):
        self.fail()

    def test_plot_graph(self):
        self.fail()
