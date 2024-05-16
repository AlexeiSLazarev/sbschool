def sum_linked_lists(ll1, ll2):
    sum_list = []
    l1 = ll1.list_vals()
    l2 = ll2.list_vals()
    if l1 and l2 and len(l1) == len(l2):
        for a, b in zip(l1,l2):
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
            if n.value and n.value == val:
                rl.append(n)
            n = n.next
        return rl

    def delete(self, val, all=False):
        n = self.head
        last_n = None
        while n:
            if n.value == val:
                if not last_n:
                    self.head = n.next
                    if not all: break
                else:
                    last_n.next = n.next
            else:
                last_n = n
            n = n.next

    def clean(self):
        if self.head: self.head = None
        if self.tail: self.tail = None

    def len(self):
        cnt = 0
        n = self.head
        while n:
            n = n.next
            cnt += 1
        return cnt

    def insert(self, afterNode, newNode):
        if newNode and not afterNode:
            newNode.next = self.head
            self.head = newNode
        else:
            n = self.find(afterNode.value)
            if n:
                n_next = n.next
                n.next = newNode
                newNode.next = n_next

    def list_vals(self):
        rl = []
        n = self.head
        while n:
            rl.append(n.value)
            n = n.next
        return rl


