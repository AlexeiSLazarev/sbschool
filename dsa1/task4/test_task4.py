import unittest
from io import StringIO

from task4 import Stack, LinkedList1d, Node


class TestStack(unittest.TestCase):

    def test_peek(self):
        stack = Stack()
        stack.push(2)
        stack.push(1)
        pop_val = stack.peek()
        self.assertEqual(pop_val, 1)
        self.assertEqual(stack.size(), 2)

    def test_pop(self):
        stack = Stack()
        stack.push(2)
        stack.push(1)
        pop_val = stack.pop()
        self.assertEqual(pop_val, 1)
        self.assertEqual(stack.size(), 1)
        pop_val = stack.pop()
        self.assertEqual(pop_val, 2)
        self.assertEqual(stack.size(), 0)

    def test_push_to_empty_stack(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.peek(), 1)

    def test_push_multiple_elements(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.peek(), 3)

    def test_pop_from_empty_stack(self):
        stack = Stack()
        self.assertIsNone(stack.pop())

    def test_pop_from_stack_with_one_element(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.size(), 0)

    def test_pop_from_stack_with_multiple_elements(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.size(), 0)
        self.assertIsNone(stack.pop())

    def test_peek_empty_stack(self):
        stack = Stack()
        self.assertIsNone(stack.peek())

    def test_peek_stack_with_one_element(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.peek(), 1)
        self.assertEqual(stack.size(), 1)

    def test_peek_stack_with_multiple_elements(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.peek(), 3)
        self.assertEqual(stack.size(), 3)

    def test_size_empty_stack(self):
        stack = Stack()
        self.assertEqual(stack.size(), 0)

    def test_size_stack_with_elements(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.size(), 1)
        stack.push(2)
        self.assertEqual(stack.size(), 2)
        stack.pop()
        self.assertEqual(stack.size(), 1)
        stack.pop()
        self.assertEqual(stack.size(), 0)

    def test_push(self):
        stack = Stack()
        stack.push(2)
        self.assertEqual(stack.size(), 1)
        stack.push(1)
        self.assertEqual(stack.size(), 2)


class TestLinkedList1d(unittest.TestCase):

    def test_delete_last(self):
        ll = LinkedList1d()
        ll.add_in_head(Node(2))
        ll.add_in_head(Node(1))
        ll.delete_last()
        self.assertEqual(ll.list_vals(), [1])

    def test_delete_first(self):
        ll = LinkedList1d()
        ll.add_in_head(Node(2))
        ll.add_in_head(Node(1))
        ll.delete_first()
        self.assertEqual(ll.list_vals(), [2])

    def test_add_in_head(self):
        ll = LinkedList1d()
        ll.add_in_head(Node(2))
        self.assertEqual(ll.list_vals(), [2])
        ll.add_in_head(Node(1))
        self.assertEqual(ll.list_vals(), [1, 2])

    def test_add_in_tail(self):
        ll = LinkedList1d()
        ll.add_in_tail(Node(1))
        self.assertEqual(ll.list_vals(), [1])
        ll.add_in_tail(Node(2))
        self.assertEqual(ll.list_vals(), [1, 2])

    def test_len(self):
        ll = LinkedList1d()
        self.assertEqual(ll.len(), 0)
        ll.add_in_tail(Node(1))
        self.assertEqual(ll.len(), 1)
        ll.add_in_tail(Node(2))
        self.assertEqual(ll.len(), 2)
        ll.delete_first()
        self.assertEqual(ll.len(), 1)
        ll.delete_last()
        self.assertEqual(ll.len(), 0)


if __name__ == "__main__":
    unittest.main()
