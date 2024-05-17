# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from dsa1.task1.task1 import *
import unittest


def create_ll(start, end) -> LinkedList:
    ll = LinkedList()
    for i in range(start, end):
        ll.add_in_tail(Node(i))
    return ll


class TestLinkedList(unittest.TestCase):

    def test_add_in_tale_nodes(self):
        ll = LinkedList()
        ll.add_in_tail(Node(12))
        ll.add_in_tail(Node(55))
        ll.add_in_tail(Node(66))
        self.assertEqual(ll.head.value, 12, "The head item should be 12")
        self.assertEqual(ll.head.next.value, 55, "The second item should be 55")
        self.assertEqual(ll.tail.value, 66, "The tail item should be 66")

    def test_delete_node_once(self):
        # Удаление одного элемента из пустого списка
        ll = LinkedList()
        ll.delete(0)
        self.assertListEqual(ll.list_vals(), [], "Empty list should remain empty.")

        # Удаление единственного элемента в списке
        ll = LinkedList()
        ll.add_in_tail(Node(0))
        ll.delete(0)
        self.assertListEqual(ll.list_vals(), [], "One element list should be empty after deletion.")
        self.assertIsNone(ll.head, "Head should be None.")
        self.assertIsNone(ll.tail, "Tail should be None.")

        # Удаление первого элемента
        ll = create_ll(0, 4)
        ll.delete(0)
        self.assertListEqual(ll.list_vals(), [1, 2, 3], "First element should be deleted.")
        self.assertEqual(ll.head.value, 1, "New head should be 1.")

        # Удаление последнего элемента
        ll = create_ll(0, 4)
        ll.delete(3)
        self.assertListEqual(ll.list_vals(), [0, 1, 2], "Last element should be deleted.")
        self.assertEqual(ll.tail.value, 2, "New tail should be 2.")

        # Удаление элемента в середине списка
        ll = create_ll(0, 4)
        ll.delete(1)
        self.assertListEqual(ll.list_vals(), [0, 2, 3], "Second element should be deleted.")

        # Удаление первого из дублирующихся элементов
        ll = LinkedList()
        ll.add_in_tail(Node(0))
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(2))
        ll.add_in_tail(Node(3))
        ll.delete(1)
        self.assertListEqual(ll.list_vals(), [0, 1, 2, 3], "First 1 should be deleted.")

    def test_delete_node_all(self):
        # Удаление всех элементов с заданным значением
        ll = LinkedList()
        ll.add_in_tail(Node(0))
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(2))
        ll.add_in_tail(Node(3))
        ll.delete(1, True)
        self.assertListEqual(ll.list_vals(), [0, 2, 3], "All 1s should be deleted.")

        ll = LinkedList()
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(2))
        ll.add_in_tail(Node(3))
        ll.delete(1, True)
        self.assertListEqual(ll.list_vals(), [2, 3], "All 1s should be deleted.")

        ll = LinkedList()
        ll.add_in_tail(Node(0))
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(2))
        ll.add_in_tail(Node(2))
        ll.add_in_tail(Node(2))
        ll.delete(2, True)
        self.assertListEqual(ll.list_vals(), [0, 1], "All 2s should be deleted.")

    def test_clean(self):
        ll = LinkedList()
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(2))
        ll.clean()
        self.assertEqual(ll.len(), 0, "The length should be 0 after clean.")
        self.assertIsNone(ll.head, "Head should be None after clean.")
        self.assertIsNone(ll.tail, "Tail should be None after clean.")

        ll = LinkedList()
        ll.clean()
        self.assertEqual(ll.len(), 0, "The length should be 0 after clean.")
        self.assertIsNone(ll.head, "Head should be None after clean.")
        self.assertIsNone(ll.tail, "Tail should be None after clean.")

    def test_find_all(self):
        ll = LinkedList()
        rl = ll.find_all(2)
        self.assertListEqual(rl, [], "Empty list should return empty result.")

        ll = LinkedList()
        n1 = Node(0)
        n2 = Node(1)
        n3 = Node(1)
        n4 = Node(2)
        ll.add_in_tail(n1)
        ll.add_in_tail(n2)
        ll.add_in_tail(n3)
        ll.add_in_tail(n4)
        rl = ll.find_all(1)
        self.assertListEqual(rl, [n2, n3], "Should find both 1s.")

        rl = ll.find_all(0)
        self.assertListEqual(rl, [n1], "Should find one 0.")

    def test_len(self):
        ll = LinkedList()
        self.assertEqual(ll.len(), 0, "The length should be 0 for an empty list.")

        ll.add_in_tail(Node(12))
        self.assertEqual(ll.len(), 1, "The length should be 1 after adding one element.")

        ll.add_in_tail(Node(55))
        self.assertEqual(ll.len(), 2, "The length should be 2 after adding two elements.")

    def test_insert_afterNode(self):
        ll = LinkedList()
        ll.insert(None, Node(5))
        self.assertListEqual(ll.list_vals(), [5], "Should insert 5 at the head.")

        ll = LinkedList()
        ll.insert(Node(1), Node(5))
        self.assertListEqual(ll.list_vals(), [], "Should do nothing if afterNode is not in list.")

        ll = LinkedList()
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(2))
        ll.add_in_tail(Node(3))
        ll.insert(None, Node(5))
        self.assertListEqual(ll.list_vals(), [5, 1, 2, 3], "Should insert 5 at the head.")

        ll = LinkedList()
        n1 = Node(0)
        n2 = Node(1)
        n3 = Node(1)
        n4 = Node(2)
        ll.add_in_tail(n1)
        ll.add_in_tail(n2)
        ll.add_in_tail(n3)
        ll.add_in_tail(n4)
        ll.insert(n2, Node(5))
        self.assertListEqual(ll.list_vals(), [0, 1, 5, 1, 2], "Should insert 5 after the first 1.")

        ll = LinkedList()
        n1 = Node(0)
        n2 = Node(1)
        n3 = Node(2)
        ll.add_in_tail(n1)
        ll.add_in_tail(n2)
        ll.add_in_tail(n3)
        ll.insert(n3, Node(5))
        self.assertListEqual(ll.list_vals(), [0, 1, 2, 5], "Should insert 5 after the last element.")

    def test_sum_two_lists(self):
        ll1 = LinkedList()
        ll1.add_in_tail(Node(1))
        ll1.add_in_tail(Node(2))
        ll1.add_in_tail(Node(3))

        ll2 = LinkedList()
        ll2.add_in_tail(Node(3))
        ll2.add_in_tail(Node(2))
        ll2.add_in_tail(Node(1))

        self.assertListEqual(sum_linked_lists(ll1, ll2), [4, 4, 4], "Should return [4, 4, 4]")

        ll1 = LinkedList()
        ll1.add_in_tail(Node(1))
        ll1.add_in_tail(Node(2))

        ll2 = LinkedList()
        ll2.add_in_tail(Node(3))
        ll2.add_in_tail(Node(2))
        ll2.add_in_tail(Node(1))

        self.assertListEqual(sum_linked_lists(ll1, ll2), [], "Should return []")


if __name__ == '__main__':
    unittest.main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
