# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from dsa1.task1 import *
import unittest


def create_ll(start, end) -> LinkedList:
    ll = LinkedList()
    for i in range(start, end):
        ll.add_in_tail(Node(i))
    return ll


class TestLinkedList(unittest.TestCase):

    def test_add_nodes(self):
        ll = LinkedList()
        ll.add_in_tail(Node(12))
        ll.add_in_tail(Node(55))
        ll.add_in_tail(Node(66))
        self.assertEqual(ll.head.value, 12, "The head item should be 12")
        self.assertEqual(ll.head.next.value, 55, "The second item should be 55")
        self.assertEqual(ll.tail.value, 66, "The tail item should be 66")

    '''
    1.1. Добавьте в класс LinkedList метод удаления одного узла по его значению
    delete(val, all=False)
    где флажок all=False по умолчанию -- удаляем только первый нашедшийся элемент.
    '''

    def test_delete_node_once(self):
        # Некорректное удаление одного элемента из пустого списка
        ll = LinkedList()
        ll.delete(0)
        self.assertListEqual(ll.list_vals(), [], "One element ll.")

        # if only one element
        # if desired node is second
        ll = LinkedList()
        ll.add_in_tail(Node(0))
        ll.delete(0)
        self.assertListEqual(ll.list_vals(), [], "One element ll.")

        # if desired node is first
        ll = create_ll(0, 4)
        ll.delete(0)
        self.assertListEqual(ll.list_vals(), [1, 2, 3], "LL. delete once. First element.")

        # if desired node is last
        ll = create_ll(0, 4)
        ll.delete(3)
        self.assertListEqual(ll.list_vals(), [0, 1, 2], "Delete last element.")

        # if desired node is second
        ll = create_ll(0, 4)
        ll.delete(1)
        self.assertListEqual(ll.list_vals(), [0, 2, 3], "Delete last element.")

        # if desired node is second
        ll = LinkedList()
        ll.add_in_tail(Node(0))
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(2))
        ll.add_in_tail(Node(3))
        ll.delete(1)
        self.assertListEqual(ll.list_vals(), [0, 1, 2, 3], "Delete last element.")

    '''
    1.2. Дополните этот метод удалением всех узлов по конкретному значению (флажок all=True).
    '''

    def test_delete_node_all(self):
        ll = LinkedList()
        ll.add_in_tail(Node(0))
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(2))
        ll.add_in_tail(Node(3))
        ll.delete(1, True)
        self.assertListEqual(ll.list_vals(), [0, 2, 3], "Delete all elements.")

        ll = LinkedList()
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(2))
        ll.add_in_tail(Node(3))
        ll.delete(1, True)
        self.assertListEqual(ll.list_vals(), [2, 3], "Delete all elements.")

        ll = LinkedList()
        ll.add_in_tail(Node(0))
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(2))
        ll.add_in_tail(Node(2))
        ll.add_in_tail(Node(2))
        ll.delete(2, True)
        self.assertListEqual(ll.list_vals(), [0, 1], "Delete all elements.")

    '''
    1.3. Добавьте в класс LinkedList метод очистки всего содержимого (создание пустого списка) -- clean()
    '''

    def test_clean(self):
        ll = LinkedList()
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(2))
        ll.clean()
        self.assertEqual(ll.len(), 0, "The length should be 0")

        ll = LinkedList()
        ll.clean()
        self.assertEqual(ll.len(), 0, "The length should be 0")

    '''
    1.4. Добавьте в класс LinkedList метод поиска всех узлов по конкретному значению (возвращается стандартный питоновский список найденных узлов).
    find_all(val)
    '''

    def test_find_all(self):
        ll = LinkedList()
        rl = ll.find_all(2)
        self.assertListEqual(rl, [])

        ll = LinkedList()
        n1 = Node(0)
        n2 = Node(1)
        n3 = Node(1)
        n4 = Node(2)
        ll.add_in_tail(n1)
        ll.add_in_tail(n2)
        ll.add_in_tail(n3)
        ll.add_in_tail(n4)
        rl = ll.find_all(0)
        self.assertListEqual(rl, [n1])

    '''
    1.5. Добавьте в класс LinkedList метод вычисления текущей длины списка -- len()
    '''

    def test_len(self):
        ll = LinkedList()
        self.assertEqual(ll.len(), 0, "The length should be 0")

        ll.add_in_tail(Node(12))
        self.assertEqual(ll.len(), 1, "The length should be 1")

        ll.add_in_tail(Node(55))
        self.assertEqual(ll.len(), 2, "The length should be 2")

    '''
    1.6. Добавьте в класс LinkedList метод вставки узла newNode после заданного узла afterNode (из списка)
    insert(afterNode, newNode)
    Если afterNode = None, добавьте новый элемент первым в списке.
    Например, имеется список (a1,a2,a3,a4,a5) и новый узел a7;
    вставляя узел a7 после узла a3, получаем список (a1,a2,a3,a7,a4,a5).
    '''

    def test_insert_afterNode(self):
        ll = LinkedList()
        ll.insert(None, Node(5))
        self.assertListEqual(ll.list_vals(), [5])

        ll.clean()
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(2))
        ll.add_in_tail(Node(3))
        ll.insert(None, Node(5))
        self.assertListEqual(ll.list_vals(), [5, 1, 2, 3])

    '''
    * 1.8. Напишите функцию, которая получает на вход два связанных списка, состоящие из целых значений, 
    и если их длины равны, возвращает список, каждый элемент которого равен сумме
    соответствующих элементов входных списков.
    '''

    def test_sum_two_lists(self):
        ll1 = LinkedList()
        ll1.add_in_tail(Node(1))
        ll1.add_in_tail(Node(2))
        ll1.add_in_tail(Node(3))

        ll2 = LinkedList()
        ll2.add_in_tail(Node(3))
        ll2.add_in_tail(Node(2))
        ll2.add_in_tail(Node(1))

        self.assertListEqual(sum_linked_lists(ll1, ll2), [4, 4, 4])



if __name__ == '__main__':
    unittest.main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
