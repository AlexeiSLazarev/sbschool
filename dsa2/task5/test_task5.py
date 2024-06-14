import unittest
from task5 import *


class TestaBST(unittest.TestCase):

    def test_add_index_minus_none(self):
        tree = aBST(3)
        self.assertEqual(tree.AddKey(4), 0)
        self.assertEqual(tree.AddKey(2), 1)

        tree = aBST(3)
        for i in [4, 2, 1, 3, 6, 5, 7]:
            tree.AddKey(i)
        self.assertEqual(tree.AddKey(16), -1)
        tree.print_tree()

    def test_add_key(self):
        tree = aBST(3)
        for i in [4, 2, 1, 3, 6, 5, 7]:
            tree.AddKey(i)
        tree.print_tree()
        # self.assertEqual(tree.AddKey(10), 0)  # добавляем 10, ожидаем 0
        # self.assertEqual(tree.AddKey(5), 1)  # добавляем 5, ожидаем 1
        # self.assertEqual(tree.AddKey(15), 2)  # добавляем 15, ожидаем 2
        # self.assertEqual(tree.AddKey(5), 1)  # добавляем 5, ожидаем 1 (уже существует)

    def test_find_key_index(self):
        tree = aBST(2)
        tree.AddKey(10)
        tree.AddKey(5)
        tree.AddKey(15)
        self.assertEqual(tree.FindKeyIndex(10), 0)  # ищем 10, ожидаем 0
        self.assertEqual(tree.FindKeyIndex(5), 1)  # ищем 5, ожидаем 1
        self.assertEqual(tree.FindKeyIndex(15), 2)  # ищем 15, ожидаем 2
        self.assertIsNone(tree.FindKeyIndex(20))  # ищем 20, ожидаем None (не найден)

    def test_tree_structure(self):
        tree = aBST(2)
        tree.AddKey(10)
        tree.AddKey(5)
        tree.AddKey(15)
        expected_tree = [10, 5, 15, None, None, None, None]
        self.assertEqual(tree.Tree, expected_tree)  # проверка структуры дерева


if __name__ == '__main__':
    unittest.main()
