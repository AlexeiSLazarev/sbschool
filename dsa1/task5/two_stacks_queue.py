from typing import Optional, List, Any
import unittest


class Node:
    def __init__(self, value: int = None):
        self.value: Any = value
        self.prev: Node = None
        self.next: Node = None


class DummyNode(Node):
    def __init__(self):
        super().__init__()


class LinkedList1d:
    def __init__(self):
        self.start_node: Node = DummyNode()
        self.start_node.prev = self.start_node
        self.start_node.next = self.start_node
        self.list_length: int = 0

    def len(self) -> int:
        return self.list_length

    def get_first(self):
        return self.start_node.next

    def get_last(self):
        return self.start_node.prev

    def delete_first(self):
        if self.len() == 0:
            return
        first_node: Node = self.start_node.next
        self.start_node.next = first_node.next
        first_node.next.prev = self.start_node
        self.list_length -= 1

    def delete_last(self):
        if self.len() == 0:
            return
        last_node: Node = self.start_node.prev
        last_node.prev.next = self.start_node
        self.start_node.prev = last_node.prev
        self.list_length -= 1

    def add_in_tail(self, new_node: Node):
        last_node: Node = self.start_node.prev
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.start_node
        self.start_node.prev = new_node
        self.list_length += 1

    def add_in_head(self, new_node: Node):
        first_node: Node = self.start_node.next
        new_node.next = first_node
        self.start_node.next = new_node
        first_node.prev = new_node
        new_node.prev = self.start_node
        self.list_length += 1

    def list_vals(self) -> List[Any]:
        return_list: List[int] = []
        current_node: Node = self.start_node.next
        while not isinstance(current_node, DummyNode):
            return_list.append(current_node.value)
            current_node = current_node.next
        return return_list


class Stack(LinkedList1d):
    def __init__(self):
        super().__init__()

    def push(self, val: Any):
        super().add_in_head(Node(val))

    def pop(self) -> Optional[Any]:
        if super().len() == 0:
            return None
        else:
            first_val: Any = super().get_first().value
            super().delete_first()
            return first_val

    def peek(self) -> Optional[Any]:
        if super().len() == 0:
            return None
        else:
            return super().get_first().value

    def size(self) -> int:
        return super().len()


class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if self.stack2.size() == 0:
            while self.stack1.size() > 0:
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def size(self):
        return self.stack1.size() + self.stack2.size()


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue_on_empty_queue(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.size(), 1)
        self.assertEqual(self.queue.stack1.peek(), 1)

    def test_enqueue_on_non_empty_queue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.size(), 3)
        self.assertEqual(self.queue.stack1.peek(), 3)

    def test_dequeue_on_empty_queue(self):
        result = self.queue.dequeue()
        self.assertIsNone(result)
        self.assertEqual(self.queue.size(), 0)

    def test_dequeue_on_queue_with_one_element(self):
        self.queue.enqueue(1)
        result = self.queue.dequeue()
        self.assertEqual(result, 1)
        self.assertEqual(self.queue.size(), 0)

    def test_dequeue_on_queue_with_multiple_elements(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        result1 = self.queue.dequeue()
        result2 = self.queue.dequeue()
        self.assertEqual(result1, 1)
        self.assertEqual(result2, 2)
        self.assertEqual(self.queue.size(), 1)
        self.assertEqual(self.queue.dequeue(), 3)

    def test_size_on_empty_queue(self):
        self.assertEqual(self.queue.size(), 0)

    def test_size_on_non_empty_queue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.size(), 3)

    def test_enqueue_dequeue_mixed_operations(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        result1 = self.queue.dequeue()
        self.queue.enqueue(3)
        result2 = self.queue.dequeue()
        result3 = self.queue.dequeue()
        self.assertEqual(result1, 1)
        self.assertEqual(result2, 2)
        self.assertEqual(result3, 3)
        self.assertEqual(self.queue.size(), 0)


if __name__ == '__main__':
    unittest.main()
