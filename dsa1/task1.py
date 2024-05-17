def sum_linked_lists(ll1, ll2):
    """
    The function takes two linked lists and if their lengths are equal,
    returns a new list where each element is the sum of corresponding elements from the input lists.
    """
    sum_list = []
    l1 = ll1.list_vals()
    l2 = ll2.list_vals()
    if l1 and l2 and len(l1) == len(l2):
        for a, b in zip(l1, l2):
            sum_list.append(a + b)
    return sum_list


class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        rl = []
        n = self.head
        while n:
            if n.value == val:
                rl.append(n)
            n = n.next
        return rl

    def get_ith_node(self, i):
        ith_node = self.head
        for i in range(i):
            # print(last.val)
            ith_node = ith_node.next
        return ith_node

    def delete_once(self, val):
        # proc head
        if self.head.value == val:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return 1
        # proc tail
        if self.tail.value == val:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                node = self.get_ith_node(self.len() - 2)
                node.next = None
                self.tail = node
            return 1
        # proc in between
        last_ne = self.head  # last_ne - last not equal to val
        n = self.head.next
        while n:
            if n.value == val:
                last_ne.next = n.next
                return 1
            else:
                last_ne = n
            n = n.next
        return 0

    def delete(self, val, all=False):
        if all:
            flag = 1
            while flag:
                flag = self.delete_once(val)
        else:
            self.delete_once(val)


    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        cnt = 0
        n = self.head
        while n:
            n = n.next
            cnt += 1
        return cnt

    def insert(self, afterNode, newNode):
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
            if not self.tail:
                self.tail = newNode
            return

        n = self.find(afterNode.value)
        if n:
            newNode.next = n.next
            n.next = newNode
            if n == self.tail:
                self.tail = newNode

    def list_vals(self):
        rl = []
        n = self.head
        while n:
            rl.append(n.value)
            n = n.next
        return rl
