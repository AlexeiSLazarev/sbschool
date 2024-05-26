from task6 import Deque
import unittest


def is_palindrome(palindrome_deque: Deque) -> bool:
    if palindrome_deque.size() <= 1:
        return True
    while palindrome_deque.size() > 1:
        if palindrome_deque.removeFront() != palindrome_deque.removeTail():
            return False
    return True


class TestIsPalindrome(unittest.TestCase):

    def test_palindrome(self):
        deque: Deque = Deque()
        self.assertEqual(is_palindrome(deque), True)

        deque.addTail("a")
        self.assertEqual(is_palindrome(deque), True)

        deque: Deque = Deque()
        for char in "aba":
            deque.addTail(char)
        self.assertEqual(is_palindrome(deque), True)

        deque: Deque = Deque()
        for char in "abba":
            deque.addTail(char)
        self.assertEqual(is_palindrome(deque), True)

        deque: Deque = Deque()
        for char in "abab":
            deque.addTail(char)
        self.assertEqual(is_palindrome(deque), False)


if __name__ == "__main__":
    unittest.main()
