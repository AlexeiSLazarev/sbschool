import unittest
from task9 import *
import unittest


class TestSimpleGraph(unittest.TestCase):

    def test_is_edge(self):
        graph = SimpleGraph(5)
        graph.AddVertex(1)
        graph.AddVertex(2)
        graph.AddEdge(0, 1)
        self.assertTrue(graph.IsEdge(0, 1))
        self.assertFalse(graph.IsEdge(1, 2))

    def test_add_vertex(self):
        graph = SimpleGraph(5)
        graph.AddVertex(1)
        graph.AddVertex(2)
        self.assertIsNotNone(graph.vertex[0])
        self.assertIsNotNone(graph.vertex[1])
        for i in range(5):
            for j in range(5):
                self.assertEqual(graph.m_adjacency[i][j], 0)

    def test_add_edge(self):
        graph = SimpleGraph(5)
        graph.AddVertex(1)
        graph.AddVertex(2)
        self.assertFalse(graph.IsEdge(0, 1))
        graph.AddEdge(0, 1)
        self.assertTrue(graph.IsEdge(0, 1))

    def test_remove_edge(self):
        graph = SimpleGraph(5)
        graph.AddVertex(1)
        graph.AddVertex(2)
        graph.AddEdge(0, 1)
        self.assertTrue(graph.IsEdge(0, 1))
        graph.RemoveEdge(0, 1)
        self.assertFalse(graph.IsEdge(0, 1))

    def test_remove_vertex(self):
        graph = SimpleGraph(5)
        graph.AddVertex(1)
        graph.AddVertex(2)
        graph.AddEdge(0, 1)
        self.assertTrue(graph.IsEdge(0, 1))
        graph.RemoveVertex(0)
        self.assertIsNone(graph.vertex[0])
        self.assertFalse(graph.IsEdge(0, 1))
        self.assertFalse(graph.IsEdge(1, 0))

    def test_common(self):
        graph = SimpleGraph(5)
        for i in range(5):
            graph.AddVertex(i)
        graph.print_adjacency_matrix()
        for i in range(5):
            graph.AddEdge(0,i)
            graph.AddEdge(i, 0)
            graph.AddEdge(3, i)
            graph.AddEdge(i, 3)
        graph.print_adjacency_matrix()
        graph.RemoveVertex(3)
        graph.print_vertex_list()
        graph.print_adjacency_matrix()
        graph.AddVertex(3)
        graph.print_vertex_list()

if __name__ == '__main__':
    unittest.main()
