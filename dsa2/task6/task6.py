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
            return True

        result = self.FindNodeByKey(key)
        if result.NodeHasKey:
            return False
        if result.ToLeft:
            result.Node.LeftChild = BSTNode(key, val, result.Node)
        else:
            result.Node.RightChild = BSTNode(key, val, result.Node)
        return True




def add_middle_to_bst(array_to_bst: List, bst: BST):
    if len(array_to_bst) == 0:
        return
    if len(array_to_bst) == 1:
        bst.AddKeyValue(array_to_bst[0], array_to_bst[0])
        return
    middle: int = len(array_to_bst) // 2
    key: int = array_to_bst[middle]
    bst.AddKeyValue(key, key)
    left_subtree = array_to_bst[:middle]
    right_subtree = array_to_bst[middle + 1:]
    add_middle_to_bst(left_subtree, bst)
    add_middle_to_bst(right_subtree, bst)


def GenerateBBSTArray(array_to_bst: list):
    bst: BST = BST(None)
    array_to_bst.sort()
    add_middle_to_bst(array_to_bst, bst)
    return bst
