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

    def delete_once(self, val: int) -> int:
        if self.head is None:
            return 0
        if self.head.value == val:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            else:
                self.head.prev = None
            return 1
        if self.tail.value == val:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                node = self.get_ith_node(self.len() - 2)
                node.next = None
                self.tail = node
            return 1
        last_ne: Optional[Node] = self.head
        n: Optional[Node] = self.head.next
        while n:
            if n.value == val:
                last_ne.next = n.next
                if n.next is not None:
                    n.next.prev = last_ne
                return 1
            else:
                last_ne = n
            n = n.next
        return 0

    def delete(self, val: int, all: bool = False):
        if all:
            flag: int = 1
            while flag:
                flag = self.delete_once(val)
        else:
            self.delete_once(val)

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
        list_len: int = self.len()
        if list_len == 0 or afterNode is None:
            if self.head is None:
                self.insert_head_empty(newNode)
            else:
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
        ith_node: Optional[Node] = self.head
        for _ in range(i):
            ith_node = ith_node.next
        return ith_node
