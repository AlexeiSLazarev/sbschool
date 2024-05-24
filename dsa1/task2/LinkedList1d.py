from typing import Optional, List
import unittest


class Node:
    def __init__(self, value: int = 0):
        self.value: int = value
        self.prev: Node = None
        self.next: Node = None


class LinkedList1d:
    def __init__(self):
        self.start_node: Node = Node()
        self.start_node.prev = self.start_node
        self.start_node.next = self.start_node
        self.list_length: int = 0

    def len(self) -> int:
        return self.list_length

    def is_start_node(self, node: Node) -> bool:
        return node is self.start_node

    def add_in_tail(self, new_node: Node):
        last_node: Node = self.start_node.prev
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.start_node
        self.start_node.prev = new_node
        self.list_length += 1

    def delete(self, val: int, all: bool = False):
        if self.len() == 0:
            return
        current_node: Node = self.start_node.next
        while not self.is_start_node(current_node):
            if current_node.value == val:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
                self.list_length -= 1
                if not all:
                    return
            current_node = current_node.next

    def list_vals(self) -> List[int]:
        return_list: List[int] = []
        current_node: Node = self.start_node.next
        while not self.is_start_node(current_node):
            return_list.append(current_node.value)
            current_node = current_node.next
        return return_list


class TestLinkedList2d(unittest.TestCase):

    def test_add_in_tail(self):
        ll = LinkedList1d()
        ll.add_in_tail(Node(1))
        self.assertEqual(ll.list_vals(), [1])
        ll.add_in_tail(Node(2))
        self.assertEqual(ll.list_vals(), [1, 2])

    def test_delete(self):
        ll = LinkedList1d()
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(2))
        ll.add_in_tail(Node(3))
        ll.delete(1)
        self.assertEqual(ll.list_vals(), [2, 3])
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(1))
        ll.delete(1, True)
        self.assertEqual(ll.list_vals(), [2, 3])

    def test_delete_empty_list(self):
        ll = LinkedList1d()
        ll.delete(1)
        self.assertEqual(ll.list_vals(), [])

    def test_delete_non_existent(self):
        ll = LinkedList1d()
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(2))
        ll.delete(3)
        self.assertEqual(ll.list_vals(), [1, 2])

    def test_len(self):
        ll = LinkedList1d()
        self.assertEqual(ll.len(), 0)
        ll.add_in_tail(Node(1))
        self.assertEqual(ll.len(), 1)
        ll.add_in_tail(Node(2))
        self.assertEqual(ll.len(), 2)
        ll.delete(1)
        self.assertEqual(ll.len(), 1)
        ll.delete(2)
        self.assertEqual(ll.len(), 0)

    def test_delete_all(self):
        ll = LinkedList1d()
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(1))
        ll.delete(1, all=True)
        self.assertEqual(ll.list_vals(), [])
        self.assertEqual(ll.len(), 0)


if __name__ == "__main__":
    unittest.main()
