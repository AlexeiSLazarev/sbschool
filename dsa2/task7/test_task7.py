import unittest
from task7 import *


class TestBalancedBST(unittest.TestCase):
    def setUp(self):
        self.bst = BalancedBST()

    def test_empty_tree(self):
        self.bst.GenerateTree([])
        self.assertIsNone(self.bst.Root)
        self.assertTrue(self.bst.IsBalanced(self.bst.Root))

    def test_single_element_tree(self):
        self.bst.GenerateTree([10])
        self.assertIsNotNone(self.bst.Root)
        self.assertEqual(self.bst.Root.NodeKey, 10)
        self.assertTrue(self.bst.IsBalanced(self.bst.Root))
        self.assertEqual(self.bst.Root.Level, 0)
        self.assertIsNone(self.bst.Root.LeftChild)
        self.assertIsNone(self.bst.Root.RightChild)

    def test_balanced_tree(self):
        self.bst.GenerateTree([30, 20, 10, 40, 50, 60, 70])
        self.assertTrue(self.bst.IsBalanced(self.bst.Root))

    def test_balanced_tree_structure(self):
        self.bst.GenerateTree([30, 20, 10, 40, 50, 60, 70])
        root = self.bst.Root
        self.assertEqual(root.NodeKey, 40)
        self.assertEqual(root.LeftChild.NodeKey, 20)
        self.assertEqual(root.RightChild.NodeKey, 60)
        self.assertEqual(root.LeftChild.LeftChild.NodeKey, 10)
        self.assertEqual(root.LeftChild.RightChild.NodeKey, 30)
        self.assertEqual(root.RightChild.RightChild.NodeKey, 70)
        self.assertEqual(root.RightChild.LeftChild.NodeKey, 50)

    def test_tree_levels(self):
        self.bst.GenerateTree([30, 20, 10, 40, 50, 60, 70])
        root = self.bst.Root
        self.assertEqual(root.Level, 0)
        self.assertEqual(root.LeftChild.Level, 1)
        self.assertEqual(root.RightChild.Level, 1)
        self.assertEqual(root.LeftChild.LeftChild.Level, 2)
        self.assertEqual(root.LeftChild.RightChild.Level, 2)
        self.assertEqual(root.RightChild.LeftChild.Level, 2)
        self.assertEqual(root.RightChild.RightChild.Level, 2)

    def test_print_bst(self):
        from random import randint
        z = [randint(0, 20) for i in range(20)]
        self.bst.GenerateTree(z)
        self.bst.print_tree()


if __name__ == '__main__':
    unittest.main()
