import os
from typing import List, Any


# 1. возведение числа N в степень M;
def power_of_number(number: int, multiplier: int) -> int:
    if multiplier == 0:
        return 1
    return number * power_of_number(number, multiplier - 1)


# 2. вычисление суммы цифр числа;
def sum_of_digits(number: int) -> int:
    def sum_digits_recursively(list_of_digits: List[int]) -> int:
        if len(list_of_digits) == 0:
            return 0
        return list_of_digits.pop() + sum_digits_recursively(list_of_digits)

    list_of_digits: List[int] = [int(digit_str) for digit_str in list(str(number))]
    return sum_digits_recursively(list_of_digits)


# 3. расчёт длины списка, для которого разрешена только операция удаления первого элемента pop(0)
# (и получение длины конечно);
def get_length_of_list(list_to_measure: List[Any]) -> int:
    if not list_to_measure:
        return 0
    return 1 + get_length_of_list(list_to_measure[1:])


# 4. проверка, является ли строка палиндромом;
def is_palindrome_recursive(suspected_str: str, first_index: int, last_index: int) -> bool:
    if first_index >= last_index:
        return True
    if suspected_str[0] == suspected_str[-1]:
        return is_palindrome_recursive(suspected_str, first_index + 1, last_index - 1)
    return False


def is_string_palindrome(suspected_str: str) -> bool:
    return is_palindrome_recursive(suspected_str, 0, len(suspected_str))


# 5. печать только чётных значений из списка;
def print_even_values(values: List[int]) -> None:
    if not values:
        return
    value = values.pop(0)
    if value % 2 == 0:
        print(value)
    print_even_values(values)


# 6. печать элементов списка с чётными индексами;
def print_even_index_values(values: List[Any], element_id: id = 1):
    if element_id >= len(values):
        return
    print(values[element_id])
    print_even_index_values(values, element_id + 2)


# 7. нахождение второго максимального числа в списке (с учётом, что максимальных может быть несколько, если они равны)
def find_second_max_value(values: List[Any], element_id: id = 0, first_max_value: int = None,
                          second_max_value: int = None):
    if element_id >= len(values):
        return second_max_value

    if first_max_value is None:
        return find_second_max_value(values, element_id + 1, values[element_id], second_max_value)
    if second_max_value is None:
        if values[element_id] > first_max_value:
            return find_second_max_value(values, element_id + 1, values[element_id], first_max_value)
        return find_second_max_value(values, element_id + 1, first_max_value, values[element_id])

    if values[element_id] >= first_max_value:
        return find_second_max_value(values, element_id + 1, values[element_id], first_max_value)
    if values[element_id] >= second_max_value:
        return find_second_max_value(values, element_id + 1, first_max_value, values[element_id])
    return find_second_max_value(values, element_id + 1, first_max_value, second_max_value)


# 8. поиск всех файлов в заданном каталоге, включая файлы, расположенные в подкаталогах произвольной вложенности.
def list_dir_recursively(folder_items: List[Any], current_path: str):
    if not folder_items:
        return []
    item = current_path + os.sep + folder_items.pop()
    if os.path.isdir(item):
        return list_dir_recursively(folder_items, current_path) + list_dir_recursively(os.listdir(item), item)
    return [item] + list_dir_recursively(folder_items, current_path)


def list_dir(dir_path: str):
    return list_dir_recursively(os.listdir(dir_path), dir_path)
