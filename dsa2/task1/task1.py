import os
from typing import List, Any, Set


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
    if list_to_measure:
        return 1 + get_length_of_list(list_to_measure[1:])
    return 0


# 4. проверка, является ли строка палиндромом;
def is_palindrome_recursive(suspected_str: str, first_index: int, last_index: int) -> bool:
    if first_index >= last_index:
        return True
    if suspected_str[first_index] != suspected_str[last_index]:
        return False
    return is_palindrome_recursive(suspected_str, first_index + 1, last_index - 1)


def is_string_palindrome(suspected_str: str) -> bool:
    return is_palindrome_recursive(suspected_str, 0, len(suspected_str) - 1)


# 5. печать только чётных значений из списка;
def print_even_values_recursively(values: List[int], item_index: int, list_length: int) -> None:
    if item_index >= list_length:
        return
    value = values[item_index]
    if value % 2 == 0:
        print(value)
    print_even_values_recursively(values, item_index + 1, list_length)


def print_even_values(values: List[int]) -> None:
    print_even_values_recursively(values, 0, len(values))


# 6. печать элементов списка с чётными индексами;
def print_even_index_values_recursively(values: List[Any], element_id: int) -> None:
    if element_id >= len(values):
        return
    print(values[element_id])
    print_even_index_values_recursively(values, element_id + 2)


def print_even_index_values(values: List[Any]):
    print_even_index_values_recursively(values, 0)


# 7. нахождение второго максимального числа в списке (с учётом, что максимальных может быть несколько, если они равны)
def find_second_max_value(values: List[Any], element_id: int, first_max_value: int, second_max_value: int) -> int:
    if element_id >= len(values):
        return second_max_value
    if values[element_id] > first_max_value:
        return find_second_max_value(values, element_id + 1, values[element_id], first_max_value)
    if second_max_value is None or values[element_id] > second_max_value:
        return find_second_max_value(values, element_id + 1, first_max_value, values[element_id])
    return find_second_max_value(values, element_id + 1, first_max_value, second_max_value)


def find_second_max(values: List[Any]) -> int:
    if not values or len(values) < 2:
        raise ValueError("List must contain at least two elements.")
    return find_second_max_value(values, 1, values[0], None)


# 8. поиск всех файлов в заданном каталоге, включая файлы, расположенные в подкаталогах произвольной вложенности.
def list_dir_recursively(folder_items: List[Any], current_path: str, current_item_id: int) -> List[Any]:
    if current_item_id >= len(folder_items):
        return []
    item = current_path + os.sep + folder_items[current_item_id]
    if os.path.isdir(item):
        return (list_dir_recursively(os.listdir(item), item, 0) +
                list_dir_recursively(folder_items, current_path, current_item_id + 1))
    return [item] + list_dir_recursively(folder_items, current_path, current_item_id + 1)


def list_dir(dir_path: str) -> List[Any]:
    final_list = list_dir_recursively(os.listdir(dir_path), dir_path, 0)
    return final_list


# Генерация всех корректных сбалансированных комбинаций круглых скобок (параметр -- количество открывающих скобок).
def generate_balanced_parenthesis_recursively(num_pairs: int, combinations: List[str], current_string: str,
                                              open_count: int, close_count: int) -> None:
    if len(current_string) == 2 * num_pairs:
        combinations.append(current_string)
        return
    if open_count < num_pairs:
        generate_balanced_parenthesis_recursively(num_pairs, combinations, current_string + '(', open_count + 1,
                                                  close_count)
    if close_count < open_count:
        generate_balanced_parenthesis_recursively(num_pairs, combinations, current_string + ')', open_count,
                                                  close_count + 1)


def generate_balanced_parenthesis(num_pairs: int) -> List[str]:
    combinations = []
    generate_balanced_parenthesis_recursively(num_pairs, combinations, '', 0, 0)
    return combinations
