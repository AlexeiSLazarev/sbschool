from collections import defaultdict, deque
from typing import List, Tuple, Set


def find_connected_subgraphs(vertices: List[int], edges: List[Tuple[int, int]]) -> List[Set[int]]:
    # Create an adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    subgraphs = []

    def bfs(start):
        queue = deque([start])
        connected_component = set()
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                connected_component.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return connected_component

    # Find all connected components
    for vertex in vertices:
        if vertex not in visited:
            subgraph = bfs(vertex)
            subgraphs.append(subgraph)

    return subgraphs


from itertools import combinations
from typing import List, Tuple


def generate_edge_combinations(edges: List[Tuple[int, int]]) -> List[List[Tuple[int, int]]]:
    all_combinations = []
    n = len(edges)

    for r in range(2, n + 1):  # Start from 2 to exclude subgraphs with less than 2 elements
        all_combinations.extend(combinations(edges, r))

    # Convert combinations from tuples to lists
    all_combinations = [list(comb) for comb in all_combinations]

    return all_combinations


def find_best_combination(vertices: List[int], edges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    edge_combinations = generate_edge_combinations(edges)
    max_even_subgraphs = 0
    best_combination = []

    for comb in edge_combinations:
        connected_subgraphs = find_connected_subgraphs(vertices, comb)
        even_subgraph_count = sum(1 for subgraph in connected_subgraphs if len(subgraph) % 2 == 0)

        if even_subgraph_count > max_even_subgraphs:
            max_even_subgraphs = even_subgraph_count
            best_combination = comb

    return best_combination

# Example usage

vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
edges = [(1, 2), (1, 3), (1, 4),
         (2, 5), (2, 6), (3, 7), (4, 8),
         (8, 9), (8, 10)]


edge_combinations = generate_edge_combinations(edges)

best_comb = []
best_comb_id = 0
max_num_subs = 0
for comb_id, comb in enumerate(edge_combinations):

    connected_subgraphs = find_connected_subgraphs(vertices, comb)
    sum_of_evens = sum(1 for subgraph in connected_subgraphs if len(subgraph) % 2 == 0)
    num_of_sub = len(connected_subgraphs)
    if sum_of_evens == num_of_sub:
        if num_of_sub > max_num_subs:
            max_num_subs = num_of_sub
            best_comb_id = comb_id
            best_comb = comb


connected_subgraphs = find_connected_subgraphs(vertices, best_comb)
print(f"Combination id: {best_comb_id}")
print(f"Combination is: {best_comb}")
edges_to_delete = list(set(edges) - set(best_comb))
print(f"Edges to delete: {edges_to_delete}")
for i, subgraph in enumerate(connected_subgraphs):
    print(f"Subgraph {i + 1}: {subgraph}")

