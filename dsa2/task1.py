from typing import List, Any


# 1. возведение числа N в степень M;
def power_of_number(number: int, multiplier: int) -> int:
    if multiplier == 0:
        return 1
    else:
        return number * power_of_number(number, multiplier - 1)


# 2. вычисление суммы цифр числа;
def sum_of_digits(number: int) -> int:
    def sum_digits_recursively(list_of_digits: List[int]) -> int:
        if len(list_of_digits) == 0:
            return 0
        else:
            return list_of_digits.pop() + sum_digits_recursively(list_of_digits)

    list_of_digits: List[int] = [int(digit_str) for digit_str in list(str(number))]
    return sum_digits_recursively(list_of_digits)


# 3. расчёт длины списка, для которого разрешена только операция удаления первого элемента pop(0)
# (и получение длины конечно);
def get_length_of_list(list_to_measure: List[Any], num_items: int = 0) -> int:
    if num_items >= len(list_to_measure):
        return num_items
    else:
        return get_length_of_list(list_to_measure, num_items + 1)


# 4. проверка, является ли строка палиндромом;
def is_string_palindrome(suspected_str: str) -> bool:
    def is_palindrome_recursive(suspected_str: str, first_index: int, last_index: int) -> bool:
        if first_index >= last_index:
            return True
        if suspected_str[0] == suspected_str[-1]:
            return is_palindrome_recursive(suspected_str, first_index + 1, last_index - 1)
        else:
            return False

    return is_palindrome_recursive(suspected_str, 0, len(suspected_str))


# 5. печать только чётных значений из списка;
def print_even_values(values: List[int], value_id: id = 0):
    if value_id >= len(values):
        return
    if values[value_id] % 2 == 0:
        print(values[value_id])
    print_even_values(values, value_id + 1)


# 6. печать элементов списка с чётными индексами;
def print_even_index_values(values: List[Any], element_id: id = 1):
    if element_id > len(values):
        return
    if element_id % 2 == 0:
        print(values[element_id - 1])
    print_even_index_values(values, element_id + 1)
