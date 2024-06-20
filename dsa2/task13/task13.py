from collections import deque
from itertools import combinations
from typing import List, Optional, Deque, Any, Tuple


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
            self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1: int, v2: int) -> None:
        if self.IsEdge(v1, v2):
            self.m_adjacency[v1][v2] = 0
            self.m_adjacency[v2][v1] = 0

    def print_adjacency_matrix(self) -> None:
        for row in self.m_adjacency:
            print(' '.join(map(str, row)))

    def print_vertex_list(self) -> None:
        print(self.get_vertex_list())

    def get_vertex_list(self) -> List[int]:
        return [i for i, v in enumerate(self.vertex) if v is not None]

    def unhit_vertexes(self):
        for v in self.vertex:
            v.Hit = False

    def get_neighbours_list(self, vertex_id: int) -> List[int]:
        neighbours_list = []
        for i in range(self.max_vertex):
            if vertex_id != i and (self.m_adjacency[vertex_id][i] == 1 or self.m_adjacency[i][vertex_id] == 1):
                neighbours_list.append(i)
        return neighbours_list

    def get_neighbor_pairs(self, neighbors: List[int]) -> List[Tuple[int, int]]:
        return list(combinations(neighbors, 2))

    def WeakVertices(self) -> List[int]:
        all_vertices = self.get_vertex_list()
        in_triangle = []
        for current_vertex in all_vertices:
            neighbours = self.get_neighbours_list(current_vertex)
            pairs = self.get_neighbor_pairs(neighbours)
            for p in pairs:
                if self.IsEdge(p[0], p[1]):
                    in_triangle.append(p)

        triangle_vertices = set()
        for pair in in_triangle:
            triangle_vertices.update(pair)

        return list(set(all_vertices) - triangle_vertices)



