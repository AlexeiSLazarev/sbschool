from random import randint

from task3 import *
import unittest


class TestBST(unittest.TestCase):

    # 1. Метод поиска

    def test_find_absent_key_root_none(self):
        bst = BST(None)
        result = bst.FindNodeByKey(7)
        self.assertIsNone(result.Node)
        self.assertFalse(result.NodeHasKey)

    def test_find_absent_key_should_return_insert_position(self):
        bst = BST(BSTNode(10, 'Root', None))
        bst.AddKeyValue(5, 'Left')

        result = bst.FindNodeByKey(7)
        self.assertFalse(result.NodeHasKey)
        self.assertFalse(result.ToLeft)
        self.assertEqual(result.Node.NodeKey, 5)

        result = bst.FindNodeByKey(17)
        self.assertFalse(result.NodeHasKey)
        self.assertFalse(result.ToLeft)
        self.assertEqual(result.Node.NodeKey, 10)

    def test_find_present_key_should_return_node(self):
        bst = BST(BSTNode(10, 'Root', None))
        bst.AddKeyValue(5, 'Left')
        bst.AddKeyValue(15, 'Right')

        result = bst.FindNodeByKey(5)
        self.assertTrue(result.NodeHasKey)
        self.assertEqual(result.Node.NodeKey, 5)

        result = bst.FindNodeByKey(15)
        self.assertTrue(result.NodeHasKey)
        self.assertEqual(result.Node.NodeKey, 15)

    # 2. Метод добавления нового узла
    def test_add_new_key_should_insert_node(self):
        bst = BST(BSTNode(10, 'Root', None))
        bst.AddKeyValue(5, 'Left')
        bst.AddKeyValue(15, 'Right')

        self.assertFalse(bst.FindNodeByKey(7).NodeHasKey)
        bst.AddKeyValue(7, 'NewNode')
        self.assertTrue(bst.FindNodeByKey(7).NodeHasKey)

        self.assertFalse(bst.FindNodeByKey(12).NodeHasKey)
        bst.AddKeyValue(12, 'NewNode')
        self.assertTrue(bst.FindNodeByKey(12).NodeHasKey)

    def test_add_existing_key_should_do_nothing(self):
        bst = BST(BSTNode(10, 'Root', None))
        bst.AddKeyValue(5, 'Left')
        bst.AddKeyValue(15, 'Right')

        result = bst.AddKeyValue(10, 'Duplicate')
        self.assertFalse(result)

    # 3. Поиск максимального и минимального ключей
    def test_find_min_max_from_root(self):
        bst = BST(BSTNode(10, 'Root', None))
        bst.AddKeyValue(5, 'Left')
        bst.AddKeyValue(15, 'Right')
        bst.AddKeyValue(2, 'LeftLeft')
        bst.AddKeyValue(17, 'RightRight')

        min_node = bst.FinMinMax(bst.Root, False)
        self.assertEqual(min_node.NodeKey, 2)

        max_node = bst.FinMinMax(bst.Root, True)
        self.assertEqual(max_node.NodeKey, 17)

    def test_find_min_max_from_subtree(self):
        bst = BST(BSTNode(10, 'Root', None))
        bst.AddKeyValue(5, 'Left')
        bst.AddKeyValue(15, 'Right')
        bst.AddKeyValue(2, 'LeftLeft')
        bst.AddKeyValue(7, 'LeftRight')
        bst.AddKeyValue(12, 'RightLeft')
        bst.AddKeyValue(17, 'RightRight')

        min_node = bst.FinMinMax(bst.FindNodeByKey(5).Node, False)
        self.assertEqual(min_node.NodeKey, 2)

        max_node = bst.FinMinMax(bst.FindNodeByKey(15).Node, True)
        self.assertEqual(max_node.NodeKey, 17)

    # 4. Метод удаления узла по его ключу
    def test_delete_node_by_key(self):
        bst = BST(BSTNode(10, 'Root', None))
        bst.AddKeyValue(5, 'Left')
        bst.AddKeyValue(15, 'Right')
        bst.AddKeyValue(2, 'LeftLeft')
        bst.AddKeyValue(7, 'LeftRight')

        self.assertTrue(bst.FindNodeByKey(5).NodeHasKey)
        bst.DeleteNodeByKey(5)
        self.assertFalse(bst.FindNodeByKey(5).NodeHasKey)
        self.assertEqual(bst.Root.LeftChild.NodeKey, 7)

    def test_delete_node_with_two_children(self):
        bst = BST(BSTNode(10, 'Root', None))
        bst.AddKeyValue(5, 'Left')
        bst.AddKeyValue(15, 'Right')
        bst.AddKeyValue(3, 'LeftLeft')
        bst.AddKeyValue(7, 'LeftRight')
        bst.AddKeyValue(6, 'LeftRightLeft')
        self.assertTrue(bst.FindNodeByKey(5).NodeHasKey)
        bst.DeleteNodeByKey(5)
        self.assertFalse(bst.FindNodeByKey(5).NodeHasKey)
        self.assertEqual(bst.Root.LeftChild.NodeKey, 6)


    def test_delete(self):
        bst = BST(BSTNode(10, 'Root', None))
        for i in range(12):
            x = randint(1,12)
            bst.AddKeyValue(x, x)
        bst.DeleteNodeByKey(5)


if __name__ == '__main__':
    unittest.main()
