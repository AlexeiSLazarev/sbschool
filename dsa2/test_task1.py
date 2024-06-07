import os
import shutil
import tempfile
import unittest
from task1 import *

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
            val = fake_out.getvalue()
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


class TestFindSecondMaxValue(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(find_second_max_value([]))

    def test_single_element_list(self):
        self.assertIsNone(find_second_max_value([1]))

    def test_all_negative_elements(self):
        self.assertEqual(find_second_max_value([-1, -2, -3, -4]), -2)

    def test_positive_elements(self):
        self.assertEqual(find_second_max_value([1, 2, 3, 4]), 3)

    def test_mixed_elements(self):
        self.assertEqual(find_second_max_value([5, 5, 4, 4, 3]), 5)

    def test_duplicate_max_values(self):
        self.assertEqual(find_second_max_value([5, 5, 4, 4, 3, 3]), 5)

    def test_duplicate_max_values_in_end(self):
        self.assertEqual(find_second_max_value([1, 2, 3, 4, 5, 5]), 5)

    def test_all_same_values(self):
        self.assertEqual(find_second_max_value([1, 1, 1, 1, 1, 1]), 1)


class TestListDir(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()

        # Create a structure of directories and files
        os.makedirs(os.path.join(self.test_dir, 'dir1'))
        os.makedirs(os.path.join(self.test_dir, 'dir2'))
        os.makedirs(os.path.join(self.test_dir, 'dir1', 'subdir1'))

        with open(os.path.join(self.test_dir, 'file1.txt'), 'w') as f:
            f.write('File 1 content')

        with open(os.path.join(self.test_dir, 'dir1', 'file2.txt'), 'w') as f:
            f.write('File 2 content')

        with open(os.path.join(self.test_dir, 'dir1', 'subdir1', 'file3.txt'), 'w') as f:
            f.write('File 3 content')

        with open(os.path.join(self.test_dir, 'dir2', 'file4.txt'), 'w') as f:
            f.write('File 4 content')

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)

    def test_list_dir(self):
        expected_files = [
            os.path.join(self.test_dir, 'file1.txt'),
            os.path.join(self.test_dir, 'dir1', 'file2.txt'),
            os.path.join(self.test_dir, 'dir1', 'subdir1', 'file3.txt'),
            os.path.join(self.test_dir, 'dir2', 'file4.txt'),
        ]
        result = list_dir(self.test_dir)
        self.assertCountEqual(result, expected_files)

    def test_list_dir_empty(self):
        empty_dir = os.path.join(self.test_dir, 'empty_dir')
        os.makedirs(empty_dir)
        result = list_dir(empty_dir)
        self.assertEqual(result, [])

    def test_list_dir_single_file(self):
        single_file_dir = os.path.join(self.test_dir, 'single_file_dir')
        os.makedirs(single_file_dir)
        file_path = os.path.join(single_file_dir, 'file.txt')
        with open(file_path, 'w') as f:
            f.write('Single file content')
        result = list_dir(single_file_dir)
        self.assertEqual(result, [file_path])


if __name__ == '__main__':
    unittest.main()
