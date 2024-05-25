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
