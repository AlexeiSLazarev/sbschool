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
def get_length_of_list(list_to_measure: List[Any]) -> int:
    def reduce_and_plus_one(list_to_measure: List[Any], num_items: int) -> int:
        if len(list_to_measure) == 0:
            return num_items
        else:
            list_to_measure.pop(0)
            return reduce_and_plus_one(list_to_measure, num_items + 1)

    return reduce_and_plus_one(list_to_measure[:], 0)  # we don't want side effects


# 4. проверка, является ли строка палиндромом;
def is_string_palindrome(suspected_str: str) -> bool:
    if len(suspected_str) in (0, 1):
        return True
    if suspected_str[0] == suspected_str[-1]:
        return is_string_palindrome(suspected_str[1:-1])
    else:
        return False


