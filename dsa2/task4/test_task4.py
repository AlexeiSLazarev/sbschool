from random import randint

from task4 import *
import unittest

from io import StringIO
import sys


class TestPrintEvenIndexValues(unittest.TestCase):
    def setUp(self):
        self.held_output = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.held_output

    def test_WideAllNodes(self):
        bst = BST(None)
        for i in [4, 2, 1, 3, 6, 5, 7]:
            bst.AddKeyValue(i, i)
        print_queue = bst.WideAllNodes()
        test_list = []
        for x in print_queue:
            test_list.append(x.NodeKey)
        self.assertListEqual(test_list, [4, 2, 6, 1, 3, 5, 7])

    def test_DeepAllNodes_in_order(self):
        bst = BST(BSTNode(4, 'Root', None))
        for i in [4, 2, 1, 3, 6, 5, 7]:
            bst.AddKeyValue(i, i)
        print_queue = bst.DeepAllNodes(0)
        test_list = []
        for x in print_queue:
            test_list.append(x.NodeKey)
        self.assertListEqual(test_list, [1, 2, 3, 4, 5, 6, 7])

    def test_DeepAllNodes_post_order(self):
        bst = BST(BSTNode(4, 'Root', None))
        for i in [4, 2, 1, 3, 6, 5, 7]:
            bst.AddKeyValue(i, i)
        print_queue = bst.DeepAllNodes(1)
        test_list = []
        for x in print_queue:
            test_list.append(x.NodeKey)
        self.assertListEqual(test_list, [1, 3, 2, 5, 7, 6, 4])

    def test_DeepAllNodes_pre_order(self):
        bst = BST(BSTNode(4, 'Root', None))
        for i in [4, 2, 1, 3, 6, 5, 7]:
            bst.AddKeyValue(i, i)
        print_queue = bst.DeepAllNodes(2)
        test_list = []
        for x in print_queue:
            test_list.append(x.NodeKey)
        self.assertListEqual(test_list, [4, 2, 1, 3, 6, 5, 7])

    def test_invert_tree(self):
        bst = BST(BSTNode(4, 'Root', None))
        for i in [4, 2, 1, 3, 6, 5, 7]:
            bst.AddKeyValue(i, i)
        # bst.print_tree()
        bst.invert_tree()
        # bst.print_tree()
        print_queue = bst.DeepAllNodes(0)
        test_list = []
        for x in print_queue:
            test_list.append(x.NodeKey)
        self.assertListEqual(test_list, [7, 6, 5, 4, 3, 2, 1])


if __name__ == '__main__':
    unittest.main()
