import unittest
from task5 import *


class TestaBST(unittest.TestCase):

    def test_add_index_minus_none(self):
        tree = aBST(2)
        self.assertEqual(tree.AddKey(4), 0)
        self.assertEqual(tree.AddKey(2), 1)

        tree = aBST(2)
        for i in [4, 2, 1, 3, 6, 5, 7]:
            tree.AddKey(i)
        result = tree.AddKey(16)
        self.assertEqual(result, -1)
        # tree.print_tree()

    def test_find_key_index(self):
        tree = aBST(2)
        for i in [4, 2, 1, 3, 6, 5, 7]:
            tree.AddKey(i)
        self.assertIsNone(tree.FindKeyIndex(15))

    def test_tree_structure(self):
        tree = aBST(2)
        tree.AddKey(10)
        tree.AddKey(5)
        tree.AddKey(15)
        expected_tree = [10, 5, 15, None, None, None, None]
        self.assertEqual(tree.Tree, expected_tree)


if __name__ == '__main__':
    unittest.main()
