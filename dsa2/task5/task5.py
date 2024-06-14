from typing import Any, List


class aBST:

    def __init__(self, depth: int):
        # правильно рассчитайте размер массива для дерева глубины depth:
        self.depth = depth
        self.tree_size = 2 ** self.depth - 1
        self.Tree: List[int] = [None] * self.tree_size  # массив ключей
        self.root = 0

    def find_recursive(self, node_index: int, key_value: int):
        if node_index >= self.tree_size:
            return None
        if self.Tree[node_index] == key_value:
            return node_index
        if self.Tree[node_index] is None:
            return -node_index

        if key_value > self.Tree[node_index]:
            next_node_index: int = self.get_right_child(node_index)
            return self.find_recursive(next_node_index, key_value)
        next_node_index: int = self.get_left_child(node_index)
        return self.find_recursive(next_node_index, key_value)

    def FindKeyIndex(self, key_value: int):
        return self.find_recursive(0, key_value)

    def AddKey(self, key):
        if self.Tree[0] is None:
            self.Tree[0] = key
            return 0
        result: int = self.FindKeyIndex(key)
        if result is not None and result <= 0:
            self.Tree[-result] = key
            return -result
        if result is not None and result > 0:
            return result
        return -1

    def get_parent(self, node_key: int):
        return (node_key - 1) / 2

    def get_left_child(self, node_key: int):
        return 2 * node_key + 1

    def get_right_child(self, node_key: int):
        return 2 * node_key + 2

    def print_tree(self) -> None:
        print("*" * 20)
        self.print_tree_recursive(0)
        print("*" * 20)

    def print_tree_recursive(self, node_index, level=0) -> None:
        if node_index >= self.tree_size:
            return
        self.print_tree_recursive(self.get_left_child(node_index), level + 1)
        print(' ' * 4 * level + '-> ' + str(self.Tree[node_index]))
        self.print_tree_recursive(self.get_right_child(node_index), level + 1)