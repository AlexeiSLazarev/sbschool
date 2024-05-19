import unittest
from task2 import Node, LinkedList2  # Replace 'your_module' with the actual module name


class TestLinkedList2(unittest.TestCase):

    def test_add_in_tail(self):
        ll = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        ll.add_in_tail(n1)
        ll.add_in_tail(n2)
        ll.add_in_tail(n3)

        self.assertEqual(ll.head, n1)
        self.assertEqual(ll.tail, n3)
        self.assertEqual(n1.next, n2)
        self.assertEqual(n2.next, n3)
        self.assertEqual(n3.next, None)
        self.assertEqual(n2.prev, n1)
        self.assertEqual(n3.prev, n2)
        self.assertEqual(n1.prev, None)

    '''
    2.1. Добавьте в класс LinkedList2 метод поиска первого узла по его значению find(val)
    '''
    def test_find(self):
        ll = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        ll.add_in_tail(n1)
        ll.add_in_tail(n2)

        self.assertEqual(ll.find(1), n1)
        self.assertEqual(ll.find(2), n2)
        self.assertEqual(ll.find(3), None)

    '''
    2.2. Добавьте в класс LinkedList2 метод поиска всех узлов по конкретному значению 
    (возвращается список найденных узлов) find_all(val)
    '''
    def test_find_all(self):
        ll = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(1)
        ll.add_in_tail(n1)
        ll.add_in_tail(n2)
        ll.add_in_tail(n3)

        self.assertEqual(ll.find_all(1), [n1, n3])
        self.assertEqual(ll.find_all(2), [n2])
        self.assertEqual(ll.find_all(3), [])

    '''
    2.3. Добавьте в класс LinkedList2 метод удаления одного узла по его значению.delete(val, all=False), 
    где флажок all=False по умолчанию -- удаляем только первый нашедшийся элемент.
    '''
    def test_delete_once(self):
        ll = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(1)
        ll.add_in_tail(n1)
        ll.add_in_tail(n2)
        ll.add_in_tail(n3)

        ll.delete(1)
        self.assertEqual(ll.find_all(1), [n3])
        self.assertEqual(n2.prev, None)
        self.assertEqual(ll.head, n2)
        self.assertEqual(ll.tail, n3)

        ll.delete(1)
        self.assertEqual(ll.find_all(1), [])
        self.assertEqual(ll.head, n2)
        self.assertEqual(ll.tail, n2)

        ll.delete(2)
        self.assertEqual(ll.head, None)
        self.assertEqual(ll.tail, None)

    '''
    2.4. Дополните этот метод удалением всех узлов по конкретному значению (флажок all=True).
    '''
    def test_delete_all(self):
        ll = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(1)
        ll.add_in_tail(n1)
        ll.add_in_tail(n2)
        ll.add_in_tail(n3)

        ll.delete(1, all=True)
        self.assertEqual(ll.find_all(1), [])
        self.assertEqual(ll.head, n2)
        self.assertEqual(ll.tail, n2)

    def test_delete_empty_list(self):
        ll = LinkedList2()
        ll.delete(1)
        self.assertEqual(ll.head, None)
        self.assertEqual(ll.tail, None)

    def test_delete_all_empty_list(self):
        ll = LinkedList2()
        ll.delete(1, all=True)
        self.assertEqual(ll.head, None)
        self.assertEqual(ll.tail, None)

    def test_delete_head(self):
        ll = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        ll.add_in_tail(n1)
        ll.add_in_tail(n2)
        ll.delete_head()

        self.assertEqual(ll.head, n2)
        self.assertEqual(ll.head.prev, None)
        self.assertEqual(ll.len(), 1)

    def test_delete_tail(self):
        ll = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        ll.add_in_tail(n1)
        ll.add_in_tail(n2)
        ll.delete_tail()

        self.assertEqual(ll.tail, n1)
        self.assertEqual(ll.tail.next, None)
        self.assertEqual(ll.len(), 1)

    def test_delete_between(self):
        ll = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        ll.add_in_tail(n1)
        ll.add_in_tail(n2)
        ll.add_in_tail(n3)
        ll.delete_between(2)

        self.assertEqual(n1.next, n3)
        self.assertEqual(n3.prev, n1)
        self.assertEqual(ll.len(), 2)

    def test_delete_one_head(self):
        ll = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        ll.add_in_tail(n1)
        ll.add_in_tail(n2)
        ll.delete_one(1)

        self.assertEqual(ll.head, n2)
        self.assertEqual(ll.head.prev, None)
        self.assertEqual(ll.len(), 1)

    def test_delete_one_tail(self):
        ll = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        ll.add_in_tail(n1)
        ll.add_in_tail(n2)
        ll.delete_one(2)

        self.assertEqual(ll.tail, n1)
        self.assertEqual(ll.tail.next, None)
        self.assertEqual(ll.len(), 1)

    def test_delete_one_between(self):
        ll = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        ll.add_in_tail(n1)
        ll.add_in_tail(n2)
        ll.add_in_tail(n3)
        ll.delete_one(2)

        self.assertEqual(n1.next, n3)
        self.assertEqual(n3.prev, n1)
        self.assertEqual(ll.len(), 2)

    def test_delete_single_node(self):
        ll = LinkedList2()
        n1 = Node(1)
        ll.add_in_tail(n1)
        ll.delete(1)

        self.assertEqual(ll.len(), 0)
        self.assertEqual(ll.head, None)
        self.assertEqual(ll.tail, None)

    def test_delete_one_not_found(self):
        ll = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        ll.add_in_tail(n1)
        ll.add_in_tail(n2)
        result = ll.delete_one(3)

        self.assertEqual(result, 0)
        self.assertEqual(ll.len(), 2)

    '''
    2.7. Добавьте в класс LinkedList2 метод очистки всего содержимого (создание пустого списка) -- clean()
    '''
    def test_clean(self):
        ll = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        ll.add_in_tail(n1)
        ll.add_in_tail(n2)

        ll.clean()
        self.assertEqual(ll.head, None)
        self.assertEqual(ll.tail, None)

    '''
    2.8. Добавьте в класс LinkedList2 метод вычисления текущей длины списка -- len()
    '''
    def test_len(self):
        ll = LinkedList2()
        self.assertEqual(ll.len(), 0)
        n1 = Node(1)
        n2 = Node(2)
        ll.add_in_tail(n1)
        ll.add_in_tail(n2)
        self.assertEqual(ll.len(), 2)

    '''
    2.5. Добавьте в класс LinkedList2 метод вставки узла после заданного узла. insert(afterNode, newNode) 
    Если afterNode = None и список пустой, добавьте новый элемент первым в списке. 
    Если afterNode = None и список непустой, добавьте новый элемент последним в списке.
    '''
    def test_insert(self):
        ll = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        ll.add_in_tail(n1)
        ll.add_in_tail(n3)

        ll.insert(n1, n2)
        llr = ll.list_vals()
        self.assertEqual(n1.next, n2)
        self.assertEqual(n2.next, n3)
        self.assertEqual(n2.prev, n1)
        self.assertEqual(n3.prev, n2)

    def test_insert_after_last(self):
        ll = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        ll.add_in_tail(n1)

        ll.insert(None, n2)
        self.assertEqual(ll.tail, n2)
        self.assertEqual(ll.tail.prev, n1)

    def test_insert_after_none_empty_list(self):
        ll = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        ll.add_in_tail(n1)

        ll.insert(None, n2)
        self.assertEqual(ll.tail, n2)
        self.assertEqual(ll.tail.prev, n1)

    def test_insert_tail_not_empty(self):
        ll = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        ll.add_in_tail(n1)
        ll.insert_tail_not_empty(n2)

        self.assertEqual(ll.tail, n2)
        self.assertEqual(ll.tail.prev, n1)
        self.assertEqual(ll.tail.next, None)
        self.assertEqual(n1.next, n2)

    def test_insert_after_tail(self):
        ll = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        ll.add_in_tail(n1)
        ll.add_in_tail(n2)
        ll.insert_after(n2, n3)

        self.assertEqual(ll.tail, n3)
        self.assertEqual(n2.next, n3)
        self.assertEqual(n3.prev, n2)
        self.assertEqual(n3.next, None)

    def test_insert_after_middle(self):
        ll = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        ll.add_in_tail(n1)
        ll.add_in_tail(n3)
        ll.insert_after(n1, n2)

        self.assertEqual(n1.next, n2)
        self.assertEqual(n2.next, n3)
        self.assertEqual(n3.prev, n2)
        self.assertEqual(n2.prev, n1)

    '''
    2.6. Добавьте в класс LinkedList2 метод вставки узла самым первым элементом. add_in_head(newNode)
    '''
    def test_add_in_head(self):
        ll = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        ll.add_in_tail(n1)

        ll.add_in_head(n2)
        self.assertEqual(ll.head, n2)
        self.assertEqual(ll.head.next, n1)
        self.assertEqual(ll.tail, n1)
        self.assertEqual(ll.tail.prev, n2)


if __name__ == '__main__':
    unittest.main()
