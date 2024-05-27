from typing import Any, List, Optional


class Node:
    def __init__(self, value: Any = None):
        self.value: Any = value
        self.prev: 'Node' = None
        self.next: 'Node' = None


class DummyNode(Node):
    def __init__(self):
        super().__init__()


class OrderedList:
    def __init__(self, asc: bool = True):
        self.init()
        self.__ascending = asc

    def init(self):
        self.start_node: Node = DummyNode()
        self.start_node.prev = self.start_node
        self.start_node.next = self.start_node
        self.list_length: int = 0

    def compare(self, v1: Any, v2: Any) -> int:
        if v1 < v2:
            return -1
        if v1 > v2:
            return 1
        return 0

    def insert_new_node_after(self, new_node: Node, left_node: Node):
        right_node: Node = left_node.next

        left_node.next = new_node
        new_node.next = right_node
        new_node.prev = left_node
        right_node.prev = new_node

        self.list_length += 1

    def insert_new_node_before(self, new_node: Node, right_node: Node):
        left_node: Node = right_node.prev

        left_node.next = new_node
        new_node.next = right_node
        new_node.prev = left_node
        right_node.prev = new_node

        self.list_length += 1

    def add(self, value: Any):
        new_node = Node(value)
        if self.len() == 0:
            self.insert_new_node_after(new_node, self.start_node)
        else:
            if self.__ascending:
                current_node: Node = self.start_node.next
                while not isinstance(current_node, DummyNode):
                    comp_res: int = self.compare(new_node.value, current_node.value)
                    if comp_res == -1 or comp_res == 0:
                        self.insert_new_node_before(new_node, current_node)
                        return
                    current_node = current_node.next
                self.insert_new_node_before(new_node, self.start_node)
            else:
                current_node: Node = self.start_node.prev
                while not isinstance(current_node, DummyNode):
                    comp_res: int = self.compare(new_node.value, current_node.value)
                    if comp_res == -1 or comp_res == 0:
                        self.insert_new_node_after(new_node, current_node)
                        return
                    current_node = current_node.prev
                self.insert_new_node_after(new_node, self.start_node)

    def find(self, val: Any) -> Optional[Any]:
        if self.len() == 0:
            return None
        current_node: Node = self.start_node.next
        while not isinstance(current_node, DummyNode):
            comp_res = self.compare(current_node.value, val)
            if comp_res == 0:
                return current_node
            if self.__ascending and comp_res == 1:
                return None
            if not self.__ascending and comp_res == -1:
                return None
            current_node = current_node.next
        return None

    def delete(self, val: Any):
        if self.len() == 0:
            return
        current_node: Node = self.start_node.next
        while not isinstance(current_node, DummyNode):
            if current_node.value == val:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
                self.list_length -= 1
                return
            current_node = current_node.next

    def clean(self, asc: bool):
        self.__ascending = asc
        self.init()

    def __len__(self) -> int:
        return self.list_length

    def len(self) -> int:
        return self.list_length

    def get_all(self) -> List[Node]:
        r = []
        if self.len() == 0:
            return r
        node = self.start_node.next
        while not isinstance(node, DummyNode):
            r.append(node)
            node = node.next
        return r

    def list_vals(self) -> List[Any]:
        return_list: List[int] = []
        if self.len() == 0:
            return return_list
        current_node: Node = self.start_node.next
        while not isinstance(current_node, DummyNode):
            return_list.append(current_node.value)
            current_node = current_node.next
        return return_list


class OrderedStringList(OrderedList):
    def __init__(self, asc: bool = True):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1: str, v2: str):
        v1 = v1.strip()
        v2 = v2.strip()
        if v1 < v2:
            return -1
        if v1 > v2:
            return 1
        return 0
