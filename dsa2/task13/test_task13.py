import unittest
from task13 import *
import unittest


class TestSimpleGraph(unittest.TestCase):

    def test_neighbours_list(self):
        graph = SimpleGraph(7)
        for i in range(7):
            graph.AddVertex(i)
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        graph.AddEdge(0, 4)
        graph.AddEdge(1, 2)
        graph.AddEdge(1, 3)
        graph.AddEdge(2, 3)
        graph.AddEdge(2, 5)
        graph.AddEdge(4, 5)
        graph.AddEdge(5, 6)

        not_in_triangle = graph.WeakVertices()

        self.assertListEqual(not_in_triangle, [4, 5, 6])


if __name__ == '__main__':
    unittest.main()
