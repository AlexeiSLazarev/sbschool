from typing import List


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
