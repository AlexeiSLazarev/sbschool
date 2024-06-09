import os
import shutil
import sys
import tempfile
import unittest
from task1 import *
from unittest.mock import patch
from io import StringIO
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


class TestPrintEvenIndexValues(unittest.TestCase):
    def setUp(self):
        self.held_output = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.held_output

    def tearDown(self):
        sys.stdout = self.original_stdout
        self.held_output.close()

    def test_empty_list(self):
        values = []
        print_even_index_values(values)
        self.assertEqual(self.held_output.getvalue(), "")

    def test_single_element(self):
        values = [10]
        print_even_index_values(values)
        self.assertEqual(self.held_output.getvalue(), "10\n")

    def test_two_elements(self):
        values = [10, 20]
        print_even_index_values(values)
        self.assertEqual(self.held_output.getvalue(), "10\n")

    def test_multiple_elements(self):
        values = [10, 20, 30, 40, 50, 60]
        print_even_index_values(values)
        self.assertEqual(self.held_output.getvalue(), "10\n30\n50\n")



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
        with self.assertRaises(ValueError):
            find_second_max([])

    def test_single_element_list(self):
        with self.assertRaises(ValueError):
            find_second_max([10])

    def test_two_elements(self):
        self.assertEqual(find_second_max([10, 20]), 10)
        self.assertEqual(find_second_max([20, 10]), 10)

    def test_multiple_elements(self):
        self.assertEqual(find_second_max([10, 20, 30, 20, 10, 50]), 30)
        self.assertEqual(find_second_max([50, 20, 30, 20, 10, 50]), 50)
        self.assertEqual(find_second_max([10, 10, 10, 10, 10, 10]), 10)
        self.assertEqual(find_second_max([10, 20, 30, 40, 50, 60]), 50)
        val = find_second_max([60, 50, 40, 30, 20, 10])
        self.assertEqual(find_second_max([60, 50, 40, 30, 20, 10]), 50)

    def test_with_duplicates(self):
        self.assertEqual(find_second_max([10, 20, 20, 20, 10, 30]), 20)
        self.assertEqual(find_second_max([30, 30, 30, 30, 30, 20]), 30)

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


class TestGenerateBalancedParenthesis(unittest.TestCase):

    def test_one_pair(self):
        self.assertListEqual(generate_balanced_parenthesis(1), ["()"])

    def test_two_pairs(self):
        self.assertEqual(set(generate_balanced_parenthesis(2)), {"(())", "()()"})

    def test_three_pairs(self):
        expected_output = {"((()))", "(()())", "(())()", "()(())", "()()()"}
        self.assertEqual(set(generate_balanced_parenthesis(3)), expected_output)

    def test_four_pairs(self):
        expected_output = {
            "(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()",
            "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"
        }
        res = set(generate_balanced_parenthesis(4))
        self.assertEqual(res, expected_output)

    def test_no_duplicates(self):
        result = generate_balanced_parenthesis(3)
        self.assertEqual(len(result), len(set(result)))


if __name__ == '__main__':
    unittest.main()
