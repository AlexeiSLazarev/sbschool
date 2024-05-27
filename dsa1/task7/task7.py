from typing import Any, List, Optional


class Node:
    def __init__(self, v: Any):
        self.value: Any = v
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None


class OrderedList:
    def __init__(self, asc: bool = True):
        self.init(asc)

    def init(self, asc: bool) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.__ascending: bool = asc
        self.list_length: int = 0

    def compare(self, v1: Any, v2: Any) -> int:
        if v1 < v2:
            return -1
        if v1 > v2:
            return 1
        return 0

    def add_in_head(self, newNode: Node) -> None:
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.list_length += 1

    def add_in_tail(self, item: Node) -> None:
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item
        self.list_length += 1

    def insert_before(self, node: Node, new_node: Node) -> None:
        if self.head == node:
            new_node.next = node
            node.prev = new_node
            self.head = new_node
        else:
            prev_node: Node = node.prev  # type: ignore
            prev_node.next = new_node
            new_node.prev = prev_node
            node.prev = new_node
            new_node.next = node
        self.list_length += 1

    def insert_after(self, node: Node, new_node: Node) -> None:
        if self.tail == node:
            new_node.prev = node
            node.next = new_node
            self.tail = new_node
        else:
            next_node: Node = node.next  # type: ignore
            next_node.prev = new_node
            new_node.next = next_node
            node.next = new_node
            new_node.prev = node
        self.list_length += 1

    def add_ascending(self, value: Any) -> None:
        new_node: Node = Node(value)
        if self.list_length == 0:
            self.add_in_tail(new_node)
            return
        current_node: Node = self.head  # type: ignore
        while current_node is not None:
            if self.compare(value, current_node.value) in (-1, 0):
                self.insert_before(current_node, new_node)
                return
            current_node = current_node.next
        self.add_in_tail(new_node)

    def add_descending(self, value: Any) -> None:
        new_node: Node = Node(value)
        if self.list_length == 0:
            self.add_in_tail(new_node)
            return
        current_node: Node = self.head  # type: ignore
        while current_node is not None:
            if self.compare(value, current_node.value) in (1, 0):
                self.insert_before(current_node, new_node)
                return
            current_node = current_node.next
        self.add_in_tail(new_node)

    def add(self, value: Any) -> None:
        if self.__ascending:
            self.add_ascending(value)
        else:
            self.add_descending(value)

    def find_ascending(self, val: Any) -> Optional[Node]:
        current_node: Node = self.head  # type: ignore
        while current_node is not None:
            if current_node.value == val:
                return current_node
            elif self.compare(current_node.value, val) == 1:
                return None
            current_node = current_node.next
        return None

    def find_descending(self, val: Any) -> Optional[Node]:
        current_node: Node = self.head  # type: ignore
        while current_node is not None:
            if current_node.value == val:
                return current_node
            elif self.compare(current_node.value, val) == -1:
                return None
            current_node = current_node.next
        return None

    def find(self, val: Any) -> Optional[Node]:
        if self.len() == 0:
            return None
        if self.__ascending:
            return self.find_ascending(val)
        return self.find_descending(val)

    def delete(self, val: Any) -> None:
        if self.list_length == 0:
            return
        node: Optional[Node] = self.find(val)
        if node is not None:
            if node == self.head:
                self.head = node.next
                if self.head:
                    self.head.prev = None
                else:
                    self.tail = None
            elif node == self.tail:
                self.tail = node.prev
                if self.tail:
                    self.tail.next = None
                else:
                    self.head = None
            else:
                prev_node: Node = node.prev  # type: ignore
                next_node: Node = node.next  # type: ignore
                prev_node.next = next_node
                next_node.prev = prev_node
            self.list_length -= 1

    def clean(self, asc: bool) -> None:
        self.init(asc)

    def len(self) -> int:
        return self.list_length

    def get_all(self) -> List[Node]:
        r: List[Node] = []
        node: Optional[Node] = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r

    def list_vals(self) -> List[Any]:
        rl: List[Any] = []
        n: Optional[Node] = self.head
        while n:
            rl.append(n.value)
            n = n.next
        return rl


class OrderedStringList(OrderedList):
    def __init__(self, asc: bool = True):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1: str, v2: str) -> int:
        v1 = v1.strip()
        v2 = v2.strip()
        if v1 < v2:
            return -1
        if v1 > v2:
            return 1
        return 0


