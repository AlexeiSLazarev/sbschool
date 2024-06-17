from typing import List, Optional, Union

class BSTNode:
    def __init__(self, key: int, parent: Optional['BSTNode'] = None):
        self.NodeKey: int = key
        self.Parent: Optional['BSTNode'] = parent
        self.LeftChild: Optional['BSTNode'] = None
        self.RightChild: Optional['BSTNode'] = None
        self.Level: int = 0


class BalancedBST:
    def __init__(self):
        self.Root: Optional[BSTNode] = None

    def GenerateTree(self, a: List[int]) -> None:
        if not a:
            return
        a.sort()
        self.Root = self._generate_balanced_bst(a, None, 0)

    def _generate_balanced_bst(self, input_array: List[int], parent: Optional[BSTNode], level: int) -> Optional[BSTNode]:
        if not input_array:
            return None
        mid_index = len(input_array) // 2
        node = BSTNode(input_array[mid_index], parent)
        node.Level = level
        node.LeftChild = self._generate_balanced_bst(input_array[:mid_index], node, level + 1)
        node.RightChild = self._generate_balanced_bst(input_array[mid_index + 1:], node, level + 1)
        return node

    def IsBalanced(self, root_node: Optional[BSTNode]) -> bool:
        if root_node is None:
            return True

        left_height = self._height(root_node.LeftChild)
        right_height = self._height(root_node.RightChild)

        if abs(left_height - right_height) > 1:
            return False

        return self.IsBalanced(root_node.LeftChild) and self.IsBalanced(root_node.RightChild)

    def _height(self, node: Optional[BSTNode]) -> int:
        if node is None:
            return 0
        left_height = self._height(node.LeftChild)
        right_height = self._height(node.RightChild)
        return max(left_height, right_height) + 1

    def print_tree(self) -> None:
        print("*" * 20)
        self.print_tree_recursive(self.Root)
        print("*" * 20)

    def print_tree_recursive(self, node: Optional[BSTNode], level: int = 0) -> None:
        if node is not None:
            self.print_tree_recursive(node.RightChild, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.NodeKey))
            self.print_tree_recursive(node.LeftChild, level + 1)


