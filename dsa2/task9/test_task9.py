import unittest
from task9 import *

import unittest


class TestSimpleGraph(unittest.TestCase):

    def test_AddVertex(self):
        g = SimpleGraph(5)
        g.AddVertex(1)
        g.AddVertex(2)
        self.assertEqual(g.vertex[0].Value, 1)
        self.assertEqual(g.vertex[1].Value, 2)
        self.assertEqual(g.num_vertex, 2)

    def test_AddEdge(self):
        g = SimpleGraph(5)
        g.AddVertex(1)
        g.AddVertex(2)
        g.AddEdge(1, 2)
        v1_id = g.find_vertex_id(1, 0)
        v2_id = g.find_vertex_id(2, 0)
        self.assertEqual(g.m_adjacency[v1_id][v2_id], 1)

    def test_RemoveEdge(self):
        g = SimpleGraph(5)
        g.AddVertex(1)
        g.AddVertex(2)
        g.AddEdge(1, 2)
        g.RemoveEdge(1, 2)
        v1_id = g.find_vertex_id(1, 0)
        v2_id = g.find_vertex_id(2, 0)
        self.assertEqual(g.m_adjacency[v1_id][v2_id], 0)

    def test_IsEdge(self):
        g = SimpleGraph(5)
        g.AddVertex(1)
        g.AddVertex(2)
        g.AddEdge(1, 2)
        self.assertTrue(g.IsEdge(1, 2))
        g.RemoveEdge(1, 2)
        self.assertFalse(g.IsEdge(1, 2))

    def test_RemoveVertex(self):
        g = SimpleGraph(5)
        print(len(g.vertex))
        g.AddVertex(1)
        g.AddVertex(2)
        g.AddVertex(3)
        g.print_vertex_list()
        g.AddEdge(1, 2)
        g.AddEdge(2, 3)
        g.AddEdge(1, 3)
        g.AddEdge(3, 1)
        g.print_adjacency_matrix()
        g.RemoveVertex(2)
        print(['*'] * 2)
        g.print_adjacency_matrix()
        g.print_vertex_list()
        print(len(g.vertex))
        self.assertEqual(g.vertex[2], None)
        self.assertFalse(g.IsEdge(1, 2))
        self.assertFalse(g.IsEdge(2, 3))
        self.assertEqual(g.num_vertex, 2)

    def test_add_vertices(self):
        g = SimpleGraph(5)
        g.AddEdge(1, 2)
        self.assertEqual(g.vertex[0].Value, 1)
        self.assertEqual(g.vertex[1].Value, 2)
        self.assertEqual(g.num_vertex, 2)

    def test_add_vertices_error(self):
        g = SimpleGraph(5)
        for i in range(10):
            g.AddVertex(i)
        g.print_vertex_list()
        g = SimpleGraph(5)
        for i in range(5):
            g.AddVertex(1)
        g.print_vertex_list()


if __name__ == '__main__':
    unittest.main()
