import unittest
from task8 import *


class TestaBST(unittest.TestCase):

    def test_add_index_minus_none(self):
        tree = Heap()
        a = [4, 2, 1, 3, 6, 5, 7]
        tree.MakeHeap(a, 2)
        self.assertListEqual(tree.get_tree_list(), [7, 4, 6, 2, 3, 1, 5])

    def test_simple(self):
        tree = Heap()
        a = [4, 2, 1, 3, 6, 5, 7]
        tree.MakeHeap(a, 2)
        tree.GetMax()
        print(tree.get_tree_list())
        self.assertListEqual(tree.get_tree_list(), [6, 4, 5, 2, 3, 1, None])


if __name__ == '__main__':
    unittest.main()
