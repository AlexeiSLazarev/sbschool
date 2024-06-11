import unittest
from task2 import *


class TestSimpleTree(unittest.TestCase):

    def test_add_child(self):
        root = SimpleTreeNode(1, None)
        tree = SimpleTree(root)
        child = SimpleTreeNode(2, root)
        tree.AddChild(root, child)
        self.assertIn(child, root.children)
        self.assertEqual(child.parent, root)

    def test_delete_node(self):
        root = SimpleTreeNode(1, None)
        tree = SimpleTree(root)
        child = SimpleTreeNode(2, root)
        tree.AddChild(root, child)
        tree.DeleteNode(child)
        self.assertNotIn(child, root.children)
        self.assertEqual(child.parent, None)

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
        self.assertIn(grandchild1, child2.children)
        self.assertEqual(grandchild1.parent, child2)
        self.assertNotIn(grandchild1, child1.children)

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


if __name__ == '__main__':
    unittest.main()
