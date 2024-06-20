import unittest
from task12 import *
import unittest


class TestSimpleGraph(unittest.TestCase):

    def test_neighbours_list(self):
        graph = SimpleGraph(6)
        for i in range(6):
            graph.AddVertex(i)
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        graph.AddEdge(1, 5)
        graph.AddEdge(2, 3)
        graph.AddEdge(2, 4)
        self.assertListEqual(graph.get_neighbours_list(2), [0, 3, 4])

    def test_DepthFirstSearch(self):
        graph = SimpleGraph(8)
        for i in range(8):
            graph.AddVertex(i)
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        graph.AddEdge(1, 5)
        graph.AddEdge(1, 6)
        graph.AddEdge(1, 7)
        graph.AddEdge(2, 3)
        graph.AddEdge(2, 4)
        vertex_list = graph.BreadthFirstSearch(6, 3)
        path_stack = [v.Value for v in vertex_list]
        self.assertListEqual(path_stack, [6, 1, 0, 2, 3])

    def test_error(self):
        graph = SimpleGraph(8)
        for i in range(8):
            graph.AddVertex(i)
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        graph.AddEdge(1, 5)
        graph.AddEdge(1, 6)
        graph.AddEdge(1, 7)
        graph.AddEdge(2, 3)
        graph.AddEdge(2, 4)
        vertex_list = graph.BreadthFirstSearch(0,1)
        path_stack = [v.Value for v in vertex_list]
        print(path_stack)


if __name__ == '__main__':
    unittest.main()
