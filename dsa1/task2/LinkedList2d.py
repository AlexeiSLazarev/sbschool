from typing import Optional, List
import unittest


class BaseNode:
    def __init__(self, v: int):
        self.value: int = v
        self.prev: Optional['BaseNode'] = None
        self.next: Optional['BaseNode'] = None


class Node(BaseNode):
    def __init__(self, v: int, dummy_flag: bool = False):
        super().__init__(v)
        self.dummy = dummy_flag


class LinkedList2d:

    def __init__(self):
        self.head: Optional[Node] = Node(0, True)
        self.tail: Optional[Node] = Node(0, True)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.list_length: int = 0

    def len(self) -> int:
        return self.list_length

    def add_in_tail(self, item: Node):
        # new to last
        self.tail.prev.next = item
        item.prev = self.tail.prev
        # new to tail
        item.next = self.tail
        self.tail.prev = item
        self.list_length += 1

    def delete_one(self, val: int) -> int:
        n: Optional[Node] = self.head.next
        while not n.dummy:
            if n.value == val:
                n.prev.next = n.next
                n.next.prev = n.prev
                self.list_length -= 1
                return 1
            n = n.next
        return 0

    def delete(self, val: int, all: bool = False):
        if self.len() == 0: return
        if all:
            while self.delete_one(val): pass
        else:
            self.delete_one(val)

    def list_vals(self) -> List[int]:
        rl: List[int] = []
        n: Optional[Node] = self.head.next
        while not n.dummy:
            rl.append(n.value)
            n = n.next
        return rl


class TestLinkedList2d(unittest.TestCase):

    def test_add_in_tail(self):
        ll = LinkedList2d()
        ll.add_in_tail(Node(1))
        self.assertEqual(ll.list_vals(), [1])
        ll.add_in_tail(Node(2))
        self.assertEqual(ll.list_vals(), [1, 2])

    def test_delete(self):
        ll = LinkedList2d()
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(2))
        ll.add_in_tail(Node(3))
        ll.delete(1)
        self.assertEqual(ll.list_vals(), [2, 3])
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(1))
        ll.delete(1, True)
        self.assertEqual(ll.list_vals(), [2, 3])


if __name__ == "__main__":
    unittest.main()
