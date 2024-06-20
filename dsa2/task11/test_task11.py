import unittest
from task11 import *
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
        vertex_list = graph.DepthFirstSearch(6, 3)
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
        vertex_list = graph.DepthFirstSearch(4, 6)
        path_stack = [v.Value for v in vertex_list]
        print(path_stack)

    def test_error2(self):
        graph = SimpleGraph(5)

        # Adding vertices
        graph.AddVertex(0)
        graph.AddVertex(1)
        graph.AddVertex(2)
        graph.AddVertex(3)
        graph.AddVertex(4)

        # Adding edges
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        graph.AddEdge(1, 3)
        # Notice that vertex 4 is isolated (no edges)

        # Printing the adjacency matrix and vertex list for verification
        graph.print_adjacency_matrix()
        graph.print_vertex_list()

        # Trying to find a path from vertex 0 to vertex 4, which should not exist
        path = graph.DepthFirstSearch(0, 4)
        print("Path from 0 to 4:", [v.Value for v in path] if path else "No path found")

        # Trying to find a path from vertex 0 to vertex 3, which should exist
        path = graph.DepthFirstSearch(0, 3)
        print("Path from 0 to 3:", [v.Value for v in path] if path else "No path found")

if __name__ == '__main__':
    unittest.main()
