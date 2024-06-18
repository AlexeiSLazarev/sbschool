from typing import List, Optional


class Vertex:
    def __init__(self, val: int):
        self.Value: int = val


class SimpleGraph:
    def __init__(self, size: int):
        self.max_vertex: int = size
        self.m_adjacency: List[List[int]] = [[0] * size for _ in range(size)]
        self.vertex: List[Optional[Vertex]] = [None] * size
        self.num_vertex: int = 0

    def AddVertex(self, v: int) -> None:
        if self.num_vertex < self.max_vertex:
            self.vertex[self.num_vertex] = Vertex(v)
            self.num_vertex += 1

    def find_edge_id(self, vertex_val: int, vertex_id: int) -> Optional[int]:
        if vertex_id >= self.num_vertex:
            return None
        if self.vertex[vertex_id] and self.vertex[vertex_id].Value == vertex_val:
            return vertex_id
        return self.find_edge_id(vertex_val, vertex_id + 1)

    def AddEdge(self, v1: int, v2: int) -> bool:
        v1_id = self.find_edge_id(v1, 0)
        v2_id = self.find_edge_id(v2, 0)
        if v1_id is not None and v2_id is not None:
            self.m_adjacency[v1_id][v2_id] = 1
            return True
        return False

    def RemoveEdge(self, v1: int, v2: int) -> bool:
        v1_id = self.find_edge_id(v1, 0)
        v2_id = self.find_edge_id(v2, 0)
        if v1_id is not None and v2_id is not None:
            self.m_adjacency[v1_id][v2_id] = 0
            return True
        return False

    def get_vertex_list(self) -> List[int]:
        return [v.Value for v in self.vertex if v is not None]

    def clean_lines(self, v_id: int) -> None:
        for i in range(self.max_vertex):
            self.m_adjacency[v_id][i] = 0
            self.m_adjacency[i][v_id] = 0

    def clean_vertex(self, v_id: int) -> None:
        self.vertex[v_id] = None
        self.num_vertex -= 1

    def shift_vertices(self, v_id: int) -> None:
        for i in range(v_id, self.num_vertex):
            self.vertex[i] = self.vertex[i + 1]
            self.vertex[i + 1] = None

    def append_matrix(self, v_id: int) -> None:
        for i in range(v_id, self.num_vertex):
            for j in range(self.max_vertex):
                self.m_adjacency[i][j] = self.m_adjacency[i + 1][j]
                self.m_adjacency[i + 1][j] = 0
            for j in range(self.max_vertex):
                self.m_adjacency[j][i] = self.m_adjacency[j][i + 1]
                self.m_adjacency[j][i + 1] = 0

    def RemoveVertex(self, v: int) -> None:
        v_id = self.find_edge_id(v, 0)
        if v_id is not None:
            self.clean_lines(v_id)
            self.clean_vertex(v_id)
            self.shift_vertices(v_id)
            self.append_matrix(v_id)

    def IsEdge(self, v1: int, v2: int) -> bool:
        v1_id = self.find_edge_id(v1, 0)
        v2_id = self.find_edge_id(v2, 0)
        if v1_id is not None and v2_id is not None and self.m_adjacency[v1_id][v2_id] == 1:
            return True
        return False

    def print_adjacency_matrix(self) -> None:
        for row in self.m_adjacency:
            print(' '.join(map(str, row)))

    def print_vertex_list(self) -> None:
        print(self.get_vertex_list())


