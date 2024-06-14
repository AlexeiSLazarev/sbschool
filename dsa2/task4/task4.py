from collections import deque
from random import randint
from typing import Any, Optional, List, Tuple


class BSTNode:

    def __init__(self, key: int, val: Any, parent: 'BSTNode'):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None


class BSTFind:

    def __init__(self, node: BSTNode, has_key: bool, to_left: bool):
        self.Node = node
        self.NodeHasKey = has_key
        self.ToLeft = to_left


class BST:

    def __init__(self, node):
        self.Root = node

    def find_node(self, node: BSTNode, key: int) -> BSTFind:
        if node.NodeKey == key:
            return BSTFind(node, True, False)

        if key < node.NodeKey and node.LeftChild is None:
            return BSTFind(node, False, to_left=True)
        if key < node.NodeKey:
            return self.find_node(node.LeftChild, key)

        if key > node.NodeKey and node.RightChild is None:
            return BSTFind(node, False, to_left=False)
        if key > node.NodeKey:
            return self.find_node(node.RightChild, key)

    def FindNodeByKey(self, key: int) -> BSTFind:

        if self.Root is None:
            return BSTFind(None, False, False)
        return self.find_node(self.Root, key)

    def AddKeyValue(self, key: int, val: Any) -> bool:
        if self.Root is None:
            self.Root = BSTNode(key, val, None)

        result = self.FindNodeByKey(key)
        if result.NodeHasKey:
            return False
        if result.ToLeft:
            result.Node.LeftChild = BSTNode(key, val, result.Node)
        else:
            result.Node.RightChild = BSTNode(key, val, result.Node)
        return True

    def FinMinMax(self, FromNode: BSTNode, FindMax: bool) -> Optional[BSTNode]:
        if FindMax and FromNode.RightChild is None:
            return FromNode
        if FindMax and FromNode.RightChild is not None:
            return self.FinMinMax(FromNode.RightChild, FindMax)

        if not FindMax and FromNode.LeftChild is None:
            return FromNode
        if not FindMax and FromNode.LeftChild is not None:
            return self.FinMinMax(FromNode.LeftChild, FindMax)

    def DeleteNodeByKey(self, key: int) -> bool:
        result = self.FindNodeByKey(key)
        if not result.NodeHasKey:
            return False
        node_to_delete = result.Node
        parent, is_left_child = self.get_parent_and_position(node_to_delete)
        # Case 1: Node to delete has no children
        if not node_to_delete.LeftChild and not node_to_delete.RightChild:
            self.remove_node_with_no_children(parent, is_left_child)
        # Case 2: Node to delete has one child
        elif node_to_delete.LeftChild and not node_to_delete.RightChild:
            self.remove_node_with_one_child(node_to_delete, parent, is_left_child, node_to_delete.LeftChild)
        elif not node_to_delete.LeftChild and node_to_delete.RightChild:
            self.remove_node_with_one_child(parent, is_left_child, node_to_delete.RightChild)
        # Case 3: Node to delete has two children
        else:
            self.remove_node_with_two_children(node_to_delete)
        return True

    def get_parent_and_position(self, node: BSTNode) -> tuple:
        parent = node.Parent
        is_left_child = (parent is not None and node == parent.LeftChild)
        return parent, is_left_child

    def remove_node_with_no_children(self, parent: Optional[BSTNode], is_left_child: bool) -> None:
        if parent is None:
            self.Root = None
        elif is_left_child:
            parent.LeftChild = None
        else:
            parent.RightChild = None

    def remove_node_with_one_child(self, parent: Optional[BSTNode], is_left_child: bool,
                                   child: Optional[BSTNode]) -> None:
        if parent is None:
            self.Root = child
        elif is_left_child:
            parent.LeftChild = child
        else:
            parent.RightChild = child
        if child is not None:
            child.Parent = parent

    def remove_node_with_two_children(self, node: BSTNode) -> None:
        successor = self.FinMinMax(node.RightChild, False)
        node.NodeKey = successor.NodeKey
        node.NodeValue = successor.NodeValue
        successor_parent = successor.Parent

        if successor_parent.LeftChild == successor:
            successor_parent.LeftChild = successor.RightChild
        else:
            successor_parent.RightChild = successor.RightChild

        if successor.RightChild is not None:
            successor.RightChild.Parent = successor_parent

    def count_nodes(self, node: Optional[BSTNode]) -> int:
        if node is None:
            return 0
        return 1 + self.count_nodes(node.LeftChild) + self.count_nodes(node.RightChild)

    def Count(self) -> int:
        return self.count_nodes(self.Root)

    def print_tree(self) -> None:
        print("*" * 20)
        self.print_tree_recursive(self.Root)
        print("*" * 20)

    def print_tree_recursive(self, node, level=0) -> None:
        if node is not None:
            self.print_tree_recursive(node.RightChild, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.NodeKey))
            self.print_tree_recursive(node.LeftChild, level + 1)

    def wide_all_queue(self, print_queue: List[Any], final_queue: List[Any]) -> None:
        if len(print_queue) <= 0:
            return
        node: BSTNode = print_queue.pop(0)
        final_queue.append(node)
        if node.LeftChild is not None:
            print_queue.append(node.LeftChild)
        if node.RightChild is not None:
            print_queue.append(node.RightChild)
        self.wide_all_queue(print_queue, final_queue)

    def WideAllNodes(self) -> tuple[Any, ...]:
        print_queue = [self.Root]
        final_queue = []
        self.wide_all_queue(print_queue, final_queue)
        return tuple(final_queue)

    def in_order_recursive(self, node, node_list: List[Any]) -> None:
        if node is not None:
            self.in_order_recursive(node.LeftChild, node_list)
            node_list.append(node)
            self.in_order_recursive(node.RightChild, node_list)
        return

    def post_order_recursive(self, node, node_list: List[Any]) -> None:
        if node is not None:
            self.post_order_recursive(node.LeftChild, node_list)
            self.post_order_recursive(node.RightChild, node_list)
            node_list.append(node)
        return

    def pre_order_recursive(self, node, node_list: List[Any]) -> None:
        if node is not None:
            node_list.append(node)
            self.pre_order_recursive(node.LeftChild, node_list)
            self.pre_order_recursive(node.RightChild, node_list)
        return

    def DeepAllNodes(self, order_key: int):

        if order_key not in (0, 1, 2):
            raise Exception("Wrong key value")
        node_list = []
        if order_key == 0:
            self.in_order_recursive(self.Root, node_list)
            return tuple(node_list)
        if order_key == 1:
            self.post_order_recursive(self.Root, node_list)
            return tuple(node_list)
        self.pre_order_recursive(self.Root, node_list)
        return tuple(node_list)

    def invert_tree_recursive(self, current_node: BSTNode):
        if current_node is None:
            return
        self.invert_tree_recursive(current_node.LeftChild)
        self.invert_tree_recursive(current_node.RightChild)
        current_node.LeftChild, current_node.RightChild = current_node.RightChild, current_node.LeftChild

    def invert_tree(self):
        self.invert_tree_recursive(self.Root)
