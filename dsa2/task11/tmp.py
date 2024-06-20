from collections import deque
from typing import List, Optional, Deque, Any


class Vertex:
    def __init__(self, val: int):
        self.Value: int = val
        self.Hit = False


class SimpleGraph:
    def __init__(self, size: int):
        self.max_vertex: int = size
        self.m_adjacency: List[List[int]] = [[0] * size for _ in range(size)]
        self.vertex: List[Optional[Vertex]] = [None] * size
        self.num_vertex: int = 0

    def AddVertex(self, v: int) -> None:
        for vertex_id in range(self.max_vertex):
            if self.vertex[vertex_id] is None:
                self.vertex[vertex_id] = Vertex(v)
                return

    def RemoveVertex(self, v: int) -> None:
        if self.is_vertex(v):
            self.vertex[v] = None
            for i in range(self.max_vertex):
                self.m_adjacency[i][v] = 0
                self.m_adjacency[v][i] = 0

    def is_in_range(self, v: int) -> bool:
        return v in range(self.max_vertex)

    def is_vertex(self, v: int) -> bool:
        return self.is_in_range(v) and self.vertex[v] is not None

    def IsEdge(self, v1: int, v2: int) -> bool:
        return self.is_vertex(v1) and self.is_vertex(v2) and self.m_adjacency[v1][v2] == 1

    def AddEdge(self, v1: int, v2: int) -> None:
        if self.is_vertex(v1) and self.is_vertex(v2):
            self.m_adjacency[v1][v2] = 1
            self.m_adjacency[v2][v1] = 1  # Assuming it's an undirected graph

    def RemoveEdge(self, v1: int, v2: int) -> None:
        if self.IsEdge(v1, v2):
            self.m_adjacency[v1][v2] = 0
            self.m_adjacency[v2][v1] = 0  # Assuming it's an undirected graph

    def print_adjacency_matrix(self) -> None:
        for row in self.m_adjacency:
            print(' '.join(map(str, row)))

    def print_vertex_list(self) -> None:
        print(self.get_vertex_list())

    def get_vertex_list(self) -> List[int]:
        return [v.Value for v in self.vertex if v is not None]

    def unhit_vertexes(self):
        for v in self.vertex:
            if v is not None:
                v.Hit = False

    def get_neighbours_list(self, vertex_id):
        neighbours_list = []
        for i in range(self.max_vertex):
            if vertex_id != i and (self.m_adjacency[vertex_id][i] == 1 or self.m_adjacency[i][vertex_id] == 1):
                neighbours_list.append(i)
        return neighbours_list

    def depth_first_search_recursive(self, path_stack: List[int], VTo: int) -> List[int]:
        if not path_stack:
            return []
        current_vertex = path_stack[-1]
        self.vertex[current_vertex].Hit = True
        if current_vertex == VTo:
            return path_stack
        neighbours_list = self.get_neighbours_list(current_vertex)
        for n in neighbours_list:
            if not self.vertex[n].Hit:
                result_path = self.depth_first_search_recursive(path_stack + [n], VTo)
                if result_path:
                    return result_path
        return []

    def DepthFirstSearch(self, VFrom: int, VTo: int) -> List[Vertex]:
        if not self.is_vertex(VFrom) or not self.is_vertex(VTo):
            return []
        self.unhit_vertexes()
        path_stack = self.depth_first_search_recursive([VFrom], VTo)
        return [self.vertex[i] for i in path_stack if path_stack]


# Example usage
graph = SimpleGraph(5)
graph.AddVertex(1)
graph.AddVertex(2)
graph.AddVertex(3)
graph.AddVertex(4)
graph.AddVertex(5)
graph.AddEdge(0, 1)
graph.AddEdge(1, 2)
graph.AddEdge(2, 3)
graph.AddEdge(3, 4)
graph.AddEdge(0, 4)
path = graph.DepthFirstSearch(0, 3)
for vertex in path:
    print(vertex.Value)
