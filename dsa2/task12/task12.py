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

    def RemoveEdge(self, v1: int, v2: int) -> None:
        if self.IsEdge(v1, v2):
            self.m_adjacency[v1][v2] = 0

    def print_adjacency_matrix(self) -> None:
        for row in self.m_adjacency:
            print(' '.join(map(str, row)))

    def print_vertex_list(self) -> None:
        print(self.get_vertex_list())

    def get_vertex_list(self) -> List[int]:
        return [v.Value for v in self.vertex if v is not None]

    def unhit_vertexes(self):
        for v in self.vertex:
            v.Hit = False

    def get_neighbours_list(self, vertex_id: int) -> List[int]:
        neighbours_list = []
        for i in range(self.max_vertex):
            if vertex_id != i and (self.m_adjacency[vertex_id][i] == 1 or self.m_adjacency[i][vertex_id] == 1):
                neighbours_list.append(i)
        return neighbours_list

    def breadth_first_search_recursive(self, vertex_queue: Deque[int], previous_nodes: dict, VTo: int) -> bool:
        if len(vertex_queue) == 0:
            return False
        current_vertex = vertex_queue.popleft()
        if current_vertex == VTo:
            return True
        self.vertex[current_vertex].Hit = True
        neighbours_list = self.get_neighbours_list(current_vertex)
        for n in neighbours_list:
            if not self.vertex[n].Hit:
                vertex_queue.append(n)
                previous_nodes[n] = current_vertex
                self.vertex[n].Hit = True
        return self.breadth_first_search_recursive(vertex_queue, previous_nodes, VTo)

    def reconstruct_path(self, previous_nodes: dict, VFrom: int, VTo: int) -> List[int]:
        path = [VTo]
        while VTo in previous_nodes:
            VTo = previous_nodes[VTo]
            path.append(VTo)
        if path[-1] == VFrom:
            return path
        return []

    def BreadthFirstSearch(self, VFrom: int, VTo: int) -> List[Vertex]:
        self.unhit_vertexes()
        vertex_queue: Deque[int] = deque([VFrom])
        previous_nodes = dict()
        found = self.breadth_first_search_recursive(vertex_queue, previous_nodes, VTo)
        if found:
            path = self.reconstruct_path(previous_nodes, VFrom, VTo)
            path.reverse()
            return [self.vertex[i] for i in path]
        return []


