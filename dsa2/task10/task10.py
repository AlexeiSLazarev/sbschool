from collections import deque, defaultdict
from typing import List, Optional, Any, Tuple, Set
from itertools import combinations


class SimpleTreeNode:
    def __init__(self, val: Any, parent: Optional['SimpleTreeNode'] = None):
        self.NodeValue = val
        self.Parent = parent
        self.Children: List['SimpleTreeNode'] = []
        self.level = 0


class SimpleTree:
    def __init__(self, root: Optional[SimpleTreeNode] = None):
        self.Root: Optional[SimpleTreeNode] = root
        self.set_levels()

    def AddChild(self, parent_node: SimpleTreeNode, new_child: SimpleTreeNode) -> None:
        if new_child.Parent and new_child in new_child.Parent.Children:
            new_child.Parent.Children.remove(new_child)
        parent_node.Children.append(new_child)
        new_child.Parent = parent_node
        self.set_levels()

    def DeleteNode(self, node_to_delete: SimpleTreeNode) -> None:
        if node_to_delete == self.Root:
            self.Root = None
        elif node_to_delete.Parent:
            node_to_delete.Parent.Children.remove(node_to_delete)
            node_to_delete.Parent = None
        self.set_levels()

    def process_node(self, node: SimpleTreeNode) -> List[SimpleTreeNode]:
        nodes = [node]
        for child in node.Children:
            nodes.extend(self.process_node(child))
        return nodes

    def GetAllNodes(self) -> List[SimpleTreeNode]:
        if self.Root is None:
            return []
        return self.process_node(self.Root)

    def FindNodesByValue(self, val: Any) -> List[SimpleTreeNode]:
        node_list: List[SimpleTreeNode] = self.GetAllNodes()
        return [node for node in node_list if node.NodeValue == val]

    def find_node_by_key(self, key: Any) -> Optional[SimpleTreeNode]:
        node_list: List[SimpleTreeNode] = self.GetAllNodes()
        for node in node_list:
            if node.NodeValue == key:
                return node
        return None

    def MoveNode(self, original_node: SimpleTreeNode, new_parent: SimpleTreeNode) -> None:
        if original_node == self.Root:
            return
        if original_node == new_parent or original_node in new_parent.Children:
            return

        if original_node.Parent:
            original_node.Parent.Children.remove(original_node)
        new_parent.Children.append(original_node)
        original_node.Parent = new_parent
        self.set_levels()

    def Count(self) -> int:
        node_list: List[SimpleTreeNode] = self.GetAllNodes()
        return len(node_list)

    def LeafCount(self) -> int:
        node_list: List[SimpleTreeNode] = self.GetAllNodes()
        num_leaf = [node for node in node_list if len(node.Children) == 0]
        return len(num_leaf)

    def set_node_level(self, node: SimpleTreeNode, level: int) -> None:
        node.level = level
        for child in node.Children:
            self.set_node_level(child, level + 1)

    def set_levels(self) -> None:
        if self.Root is not None:
            self.set_node_level(self.Root, 0)

    def print_tree(self) -> None:
        self.print_tree_recursive(self.Root)
        print("*" * 10)

    def print_tree_recursive(self, node: SimpleTreeNode, level=0) -> List[SimpleTreeNode]:
        if node is not None:
            print(' ' * 4 * level + '-> ' + str(node.NodeValue))
            nodes = [node]
            for child in node.Children:
                # print(' ' * 4 * level + '-> ' + str(node.NodeValue))
                self.print_tree_recursive(child, level + 1)
            return nodes

    def get_all_edges(self) -> List[Tuple[SimpleTreeNode, SimpleTreeNode]]:
        edges = []
        if self.Root is not None:
            nodes = self.GetAllNodes()
            for node in nodes:
                for child in node.Children:
                    edges.append((node, child))
        return edges

    def get_all_edge_combinations(self) -> List[List[Tuple[SimpleTreeNode, SimpleTreeNode]]]:
        all_edges = self.get_all_edges()
        edge_combinations = []

        for r in range(1, len(all_edges) + 1):
            edge_combinations.extend(combinations(all_edges, r))

        return edge_combinations

    def find_connected_subgraphs(self, vertices: List[int], edges: List[Tuple[int, int]]) -> List[Set[int]]:
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

    def generate_edge_combinations(self, edges: List[Tuple[int, int]]) -> List[List[Tuple[int, int]]]:
        all_combinations = []
        n = len(edges)

        for r in range(2, n + 1):  # Start from 2 to exclude subgraphs with less than 2 elements
            all_combinations.extend(combinations(edges, r))

        # Convert combinations from tuples to lists
        all_combinations = [list(comb) for comb in all_combinations]

        return all_combinations

    def find_best_combination(self, vertices: List[int], edges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        edge_combinations = self.generate_edge_combinations(edges)
        max_even_subgraphs = 0
        best_combination = []

        for comb in edge_combinations:
            connected_subgraphs = self.find_connected_subgraphs(vertices, comb)
            even_subgraph_count = sum(1 for subgraph in connected_subgraphs if len(subgraph) % 2 == 0)

            if even_subgraph_count > max_even_subgraphs:
                max_even_subgraphs = even_subgraph_count
                best_combination = comb

        return best_combination

    def find_edges_to_delete(self, edges, vertices):
        edge_combinations = self.generate_edge_combinations(edges)
        best_comb = []
        max_num_subs = 0
        for comb_id, comb in enumerate(edge_combinations):
            connected_subgraphs = self.find_connected_subgraphs(vertices, comb)
            sum_of_evens = sum(1 for subgraph in connected_subgraphs if len(subgraph) % 2 == 0)
            num_of_sub = len(connected_subgraphs)
            if sum_of_evens == num_of_sub:
                if num_of_sub > max_num_subs:
                    max_num_subs = num_of_sub
                    best_comb = comb
        return list(set(edges) - set(best_comb))

    def convert_edges_keys_to_objects(self, edges):
        real_edges = [(self.find_node_by_key(edge[0]), self.find_node_by_key(edge[1])) for edge in edges]
        return real_edges

    def EvenTrees(self):
        vertex_list = self.GetAllNodes()
        vertices = [node.NodeValue for node in vertex_list]
        edge_list = self.get_all_edges()
        edges = [(edge[0].NodeValue, edge[1].NodeValue) for edge in edge_list]
        edges_to_delete = self.find_edges_to_delete(edges, vertices)
        return self.convert_edges_keys_to_objects(edges_to_delete)
