import unittest
from task1 import power_of_number, \
    sum_of_digits, \
    get_length_of_list, \
    is_string_palindrome, \
    print_even_values, \
    print_even_index_values

from unittest.mock import patch
import io

class TestMultiplyNumber(unittest.TestCase):

    def test_power_of_number_base_case(self):
        self.assertEqual(power_of_number(2, 0), 1)
        self.assertEqual(power_of_number(5, 0), 1)
        self.assertEqual(power_of_number(2, 2), 4)
        self.assertEqual(power_of_number(-1, 2), 1)

    def test_power_of_number_positive_multiplier(self):
        self.assertEqual(power_of_number(2, 3), 8)
        self.assertEqual(power_of_number(5, 2), 25)
        self.assertEqual(power_of_number(3, 4), 81)

    def test_power_of_number_edge_cases(self):
        self.assertEqual(power_of_number(1, 10), 1)
        self.assertEqual(power_of_number(0, 5), 0)

    def test_power_of_number_large_numbers(self):
        self.assertEqual(power_of_number(2, 10), 1024)
        self.assertEqual(power_of_number(10, 3), 1000)


class TestSumOfDigits(unittest.TestCase):
    def test_sum_of_digits_single_digit(self):
        self.assertEqual(sum_of_digits(0), 0)
        self.assertEqual(sum_of_digits(5), 5)

    def test_sum_of_digits_multiple_digits(self):
        self.assertEqual(sum_of_digits(123), 6)
        self.assertEqual(sum_of_digits(456), 15)
        self.assertEqual(sum_of_digits(789), 24)

    def test_sum_of_digits_large_number(self):
        self.assertEqual(sum_of_digits(1234567890), 45)
        self.assertEqual(sum_of_digits(9876543210), 45)

    def test_sum_of_digits_repeated_digits(self):
        self.assertEqual(sum_of_digits(11111), 5)
        self.assertEqual(sum_of_digits(22222), 10)


class TestGetLengthOfList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(get_length_of_list([]), 0)

    def test_single_element_list(self):
        self.assertEqual(get_length_of_list([42]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(get_length_of_list([1, 2, 3, 4, 5]), 5)

    def test_list_with_none_elements(self):
        self.assertEqual(get_length_of_list([None, None, None]), 3)

    def test_list_with_mixed_elements(self):
        self.assertEqual(get_length_of_list([1, 'two', 3.0, [4], {5: 'five'}]), 5)

    def test_list_not_modified(self):
        original_list = [1, 2, 3]
        get_length_of_list(original_list)
        self.assertEqual(original_list, [1, 2, 3])

# Test suite for the function
class TestIsStringPalindrome(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(is_string_palindrome(""))

    def test_single_character_string(self):
        self.assertTrue(is_string_palindrome("a"))

    def test_palindrome_even_length(self):
        self.assertTrue(is_string_palindrome("abba"))

    def test_palindrome_odd_length(self):
        self.assertFalse(is_string_palindrome("acdc"))

    def test_not_palindrome(self):
        self.assertFalse(is_string_palindrome("hello"))

    def test_palindrome_with_mixed_case(self):
        self.assertFalse(is_string_palindrome("Aba"))


class TestPrintEvenIndexElements(unittest.TestCase):

    def test_empty_list(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            print_even_index_values([])
            self.assertEqual(fake_out.getvalue(), "")

    def test_single_element(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            print_even_index_values([1])
            self.assertEqual(fake_out.getvalue(), "")

    def test_two_elements(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            print_even_index_values([1, 2])
            self.assertEqual(fake_out.getvalue(), "2\n")

    def test_multiple_elements(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            print_even_index_values([10, 20, 30, 40, 50])
            self.assertEqual(fake_out.getvalue(), "20\n40\n")

    def test_all_even_positions(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            print_even_index_values([2, 4, 6, 8, 10, 12, 14])
            self.assertEqual(fake_out.getvalue(), "4\n8\n12\n")

    def test_strings(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            print_even_index_values(["a", "b", "c", "d", "e", "f"])
            self.assertEqual(fake_out.getvalue(), "b\nd\nf\n")

    def test_mixed_types(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            print_even_index_values([1, "two", 3.0, "four", 5, "six"])
            self.assertEqual(fake_out.getvalue(), "two\nfour\nsix\n")


class TestPrintEvenValues(unittest.TestCase):

    def test_empty_list(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            print_even_values([])
            self.assertEqual(fake_out.getvalue(), "")

    def test_single_odd_element(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            print_even_values([1])
            self.assertEqual(fake_out.getvalue(), "")

    def test_single_even_element(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            print_even_values([2])
            self.assertEqual(fake_out.getvalue(), "2\n")

    def test_two_elements(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            print_even_values([1, 2])
            self.assertEqual(fake_out.getvalue(), "2\n")

    def test_multiple_elements(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            print_even_values([10, 15, 20, 25, 30])
            self.assertEqual(fake_out.getvalue(), "10\n20\n30\n")

    def test_all_odd_elements(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            print_even_values([1, 3, 5, 7, 9])
            self.assertEqual(fake_out.getvalue(), "")

    def test_all_even_elements(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            print_even_values([2, 4, 6, 8, 10])
            self.assertEqual(fake_out.getvalue(), "2\n4\n6\n8\n10\n")

    def test_mixed_even_odd_elements(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            print_even_values([1, 2, 3, 4, 5, 6])
            self.assertEqual(fake_out.getvalue(), "2\n4\n6\n")

    def test_negative_even_elements(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            print_even_values([-2, -4, -6, -8])
            self.assertEqual(fake_out.getvalue(), "-2\n-4\n-6\n-8\n")

    def test_negative_odd_elements(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            print_even_values([-1, -3, -5])
            self.assertEqual(fake_out.getvalue(), "")

    def test_mixed_sign_elements(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            print_even_values([2, -3, 4, -5, 6, -7])
            self.assertEqual(fake_out.getvalue(), "2\n4\n6\n")

if __name__ == '__main__':
    unittest.main()
