import unittest
from task10 import *


class TestTmp(unittest.TestCase):

    def test_all_exampl2(self):
        node1 = SimpleTreeNode(1)
        tree = SimpleTree(node1)
        node2 = SimpleTreeNode(2)
        node3 = SimpleTreeNode(3)
        node4 = SimpleTreeNode(4)

        tree.AddChild(tree.Root, node2)
        tree.AddChild(tree.Root, node3)

        tree.AddChild(node3, node4)

        edges = tree.EvenTrees()
        result = [(edge[0].NodeValue, edge[1].NodeValue) for edge in edges]
        self.assertListEqual(result, [(1, 3)])

    def test_example1(self):
        node1 = SimpleTreeNode(1)
        tree = SimpleTree(node1)
        node2 = SimpleTreeNode(2)
        node3 = SimpleTreeNode(3)
        node4 = SimpleTreeNode(4)
        node5 = SimpleTreeNode(5)
        node6 = SimpleTreeNode(6)
        node7 = SimpleTreeNode(7)
        node8 = SimpleTreeNode(8)
        node9 = SimpleTreeNode(9)
        node10 = SimpleTreeNode(10)

        tree.AddChild(tree.Root, node2)
        tree.AddChild(tree.Root, node3)
        tree.AddChild(tree.Root, node4)

        tree.AddChild(node2, node5)
        tree.AddChild(node2, node6)

        tree.AddChild(node3, node7)
        tree.AddChild(node4, node8)

        tree.AddChild(node8, node9)
        tree.AddChild(node8, node10)

        edges = tree.EvenTrees()
        result = [(edge[0].NodeValue, edge[1].NodeValue) for edge in edges]
        self.assertListEqual(result, [(1, 3), (1, 4)])


if __name__ == '__main__':
    unittest.main()
