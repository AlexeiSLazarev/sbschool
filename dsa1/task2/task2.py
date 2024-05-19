from typing import List, Optional


class Node:
    def __init__(self, v: int):
        self.value: int = v
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None


class LinkedList2:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def add_in_tail(self, item: Node):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val: int) -> Optional[Node]:
        node: Optional[Node] = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val: int) -> List[Node]:
        rl: List[Node] = []
        n: Optional[Node] = self.head
        while n:
            if n.value == val:
                rl.append(n)
            n = n.next
        return rl

    def delete_head(self):
        self.head.next.prev = None
        self.head = self.head.next
        return 1

    def delete_tail(self):
        self.tail.prev.next = None
        self.tail = self.tail.prev
        return 1

    def delete_between(self, val):
        n: Optional[Node] = self.head.next
        while n:
            if n.value == val:
                n.next.prev = n.prev
                n.prev.next = n.next
                return 1
            n = n.next
        return 0

    def delete_one(self, val: int) -> int:
        if self.head is None:
            return 0

        if self.len() == 1 and self.head.value == val:
            self.head = None
            self.tail = None
            return 0

        if self.head.value == val: return self.delete_head()
        if self.tail.value == val: return self.delete_tail()

        return self.delete_between(val)

    def delete(self, val: int, all: bool = False):
        if self.len() == 0: return
        if all:
            while self.delete_one(val): pass
        else:
            self.delete_one(val)

    def clean(self):
        self.head = None
        self.tail = None

    def len(self) -> int:
        cnt: int = 0
        n: Optional[Node] = self.head
        while n:
            n = n.next
            cnt += 1
        return cnt

    def insert_head_empty(self, newNode: Node):
        self.head = newNode
        self.tail = newNode

    def insert_tail_not_empty(self, newNode: Node):
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode

    def insert_after(self, afterNode: Node, newNode: Node):
        n: Optional[Node] = self.find(afterNode.value)
        if n:
            newNode.next = n.next
            newNode.prev = n
            if n.next is not None:
                n.next.prev = newNode
            n.next = newNode
            if n == self.tail:
                self.tail = newNode

    def insert(self, afterNode: Optional[Node], newNode: Node):
        if self.head is None:
            self.insert_head_empty(newNode)
            return

        if afterNode is None:
            self.insert_tail_not_empty(newNode)
            return

        self.insert_after(afterNode, newNode)

    def add_in_head(self, newNode: Node):
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def list_vals(self) -> List[int]:
        rl: List[int] = []
        n: Optional[Node] = self.head
        while n:
            rl.append(n.value)
            n = n.next
        return rl

    def get_ith_node(self, i: int) -> Optional[Node]:
        if i < 0:
            return None
        ith_node: Optional[Node] = self.head
        for _ in range(i):
            if ith_node is None:
                return None
            ith_node = ith_node.next
        return ith_node
