import unittest
from task2 import *


class TestSimpleTree(unittest.TestCase):

    def test_add_child(self):
        root = SimpleTreeNode(1, None)
        tree = SimpleTree(root)
        child = SimpleTreeNode(2, root)
        tree.AddChild(root, child)
        self.assertIn(child, root.Children)
        self.assertEqual(child.Parent, root)

    def test_delete_node(self):
        root = SimpleTreeNode(1, None)
        tree = SimpleTree(root)
        child = SimpleTreeNode(2, root)
        tree.AddChild(root, child)
        tree.DeleteNode(child)
        self.assertNotIn(child, root.Children)
        self.assertEqual(child.Parent, None)

    def test_get_all_nodes(self):
        root = SimpleTreeNode(1, None)
        tree = SimpleTree(root)
        child1 = SimpleTreeNode(2, root)
        child2 = SimpleTreeNode(3, root)
        tree.AddChild(root, child1)
        tree.AddChild(root, child2)
        grandchild1 = SimpleTreeNode(4, child1)
        tree.AddChild(child1, grandchild1)
        nodes = tree.GetAllNodes()
        self.assertEqual(len(nodes), 4)
        self.assertIn(root, nodes)
        self.assertIn(child1, nodes)
        self.assertIn(child2, nodes)
        self.assertIn(grandchild1, nodes)

    def test_find_nodes_by_value(self):
        root = SimpleTreeNode(1, None)
        tree = SimpleTree(root)
        child1 = SimpleTreeNode(2, root)
        child2 = SimpleTreeNode(3, root)
        tree.AddChild(root, child1)
        tree.AddChild(root, child2)
        nodes = tree.FindNodesByValue(2)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0], child1)

    def test_move_node(self):
        root = SimpleTreeNode(1, None)
        tree = SimpleTree(root)
        child1 = SimpleTreeNode(2, root)
        child2 = SimpleTreeNode(3, root)
        tree.AddChild(root, child1)
        tree.AddChild(root, child2)
        grandchild1 = SimpleTreeNode(4, child1)
        tree.AddChild(child1, grandchild1)
        tree.MoveNode(grandchild1, child2)
        self.assertIn(grandchild1, child2.Children)
        self.assertEqual(grandchild1.Parent, child2)
        self.assertNotIn(grandchild1, child1.Children)

    def test_count(self):
        root = SimpleTreeNode(1, None)
        tree = SimpleTree(root)
        child1 = SimpleTreeNode(2, root)
        child2 = SimpleTreeNode(3, root)
        tree.AddChild(root, child1)
        tree.AddChild(root, child2)
        grandchild1 = SimpleTreeNode(4, child1)
        tree.AddChild(child1, grandchild1)
        self.assertEqual(tree.Count(), 4)
        new_child = SimpleTreeNode(5, child2)
        tree.AddChild(child2, new_child)
        self.assertEqual(tree.Count(), 5)

    def test_leaf_count(self):
        root = SimpleTreeNode(1, None)
        tree = SimpleTree(root)
        child1 = SimpleTreeNode(2, root)
        child2 = SimpleTreeNode(3, root)
        tree.AddChild(root, child1)
        tree.AddChild(root, child2)
        grandchild1 = SimpleTreeNode(4, child1)
        tree.AddChild(child1, grandchild1)
        self.assertEqual(tree.LeafCount(), 2)
        new_child = SimpleTreeNode(5, child2)
        tree.AddChild(child1, new_child)
        self.assertEqual(tree.LeafCount(), 3)


class TestSimpleTree2(unittest.TestCase):

    def setUp(self) -> None:
        self.root = SimpleTreeNode(0)
        self.tree = SimpleTree(self.root)

    def test_add_child(self) -> None:
        child = SimpleTreeNode(1)
        self.tree.AddChild(self.root, child)
        self.assertIn(child, self.root.Children)
        self.assertEqual(child.Parent, self.root)

    def test_delete_node(self) -> None:
        child = SimpleTreeNode(1)
        self.tree.AddChild(self.root, child)
        self.tree.DeleteNode(child)
        self.assertNotIn(child, self.root.Children)
        self.assertIsNone(child.Parent)

    def test_get_all_nodes(self) -> None:
        child1 = SimpleTreeNode(1)
        child2 = SimpleTreeNode(2)
        self.tree.AddChild(self.root, child1)
        self.tree.AddChild(self.root, child2)
        all_nodes = self.tree.GetAllNodes()
        self.assertEqual(len(all_nodes), 3)
        self.assertIn(self.root, all_nodes)
        self.assertIn(child1, all_nodes)
        self.assertIn(child2, all_nodes)

    def test_find_nodes_by_value(self) -> None:
        child1 = SimpleTreeNode(1)
        child2 = SimpleTreeNode(2)
        child3 = SimpleTreeNode(1)
        self.tree.AddChild(self.root, child1)
        self.tree.AddChild(self.root, child2)
        self.tree.AddChild(self.root, child3)
        nodes_with_value_1 = self.tree.FindNodesByValue(1)
        self.assertEqual(len(nodes_with_value_1), 2)
        self.assertIn(child1, nodes_with_value_1)
        self.assertIn(child3, nodes_with_value_1)

    def test_move_node(self) -> None:
        child1 = SimpleTreeNode(1)
        child2 = SimpleTreeNode(2)
        self.tree.AddChild(self.root, child1)
        self.tree.AddChild(self.root, child2)
        self.tree.MoveNode(child1, child2)
        self.assertNotIn(child1, self.root.Children)
        self.assertIn(child1, child2.Children)
        self.assertEqual(child1.Parent, child2)

    def test_count(self) -> None:
        child1 = SimpleTreeNode(1)
        child2 = SimpleTreeNode(2)
        self.tree.AddChild(self.root, child1)
        self.tree.AddChild(self.root, child2)
        self.assertEqual(self.tree.Count(), 3)

    def test_leaf_count(self) -> None:
        child1 = SimpleTreeNode(1)
        child2 = SimpleTreeNode(2)
        self.tree.AddChild(self.root, child1)
        self.tree.AddChild(self.root, child2)
        self.assertEqual(self.tree.LeafCount(), 2)
        child3 = SimpleTreeNode(3)
        self.tree.AddChild(child1, child3)
        self.assertEqual(self.tree.LeafCount(), 2)

    def test_set_levels(self) -> None:
        child1 = SimpleTreeNode(1)
        child2 = SimpleTreeNode(2)
        self.tree.AddChild(self.root, child1)
        self.tree.AddChild(child1, child2)
        self.tree.set_levels()
        self.assertEqual(self.root.level, 0)
        self.assertEqual(child1.level, 1)
        self.assertEqual(child2.level, 2)


class TestErrors(unittest.TestCase):
    def setUp(self) -> None:
        self.root = SimpleTreeNode(0)
        self.tree = SimpleTree(self.root)

    def test_find_by_value(self):
        '''
        Исключение при обращении к NodeValue после FindNodesByValue
        '''
        root = SimpleTreeNode(0, None)
        tree = SimpleTree(root)
        search_value: int = 3
        child1 = SimpleTreeNode(search_value, root)
        child2 = SimpleTreeNode(search_value, root)
        child3 = SimpleTreeNode(search_value, root)
        child4 = SimpleTreeNode(search_value, root)
        tree.AddChild(root, child1)
        tree.AddChild(root, child2)
        tree.AddChild(root, child3)
        tree.AddChild(child1, child4)
        search_value: int = 3
        node_list: List[SimpleTreeNode] = tree.FindNodesByValue(search_value)
        for node in node_list:
            self.assertEqual(node.NodeValue, search_value)
        self.assertEqual(len(node_list), 4)

    def test_find_nodes_by_value(self) -> None:
        child1 = SimpleTreeNode(1)
        child2 = SimpleTreeNode(2)
        child3 = SimpleTreeNode(1)
        self.tree.AddChild(self.root, child1)
        self.tree.AddChild(self.root, child2)
        self.tree.AddChild(self.root, child3)
        nodes_with_value_1 = self.tree.FindNodesByValue(1)
        self.assertEqual(len(nodes_with_value_1), 2)
        self.assertIn(child1, nodes_with_value_1)
        self.assertIn(child3, nodes_with_value_1)


if __name__ == '__main__':
    unittest.main()
