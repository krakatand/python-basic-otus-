"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number**2 for number in numbers]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):
    """
    функция, которая принимает число, и возвращает ответ Тру,
    если число простое
    >>> is_prime(7)
    <<< True
    """
    if number == 1:
        return True
    else:
        count = 0
        for i in range(number + 1):
            if number % i == 0:
                count += 1
            else:
                continue
        return count == 2


def filter_numbers(numbers_list, filter):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter == ODD:
        return [number for number in numbers_list if number % 2]
    if filter == EVEN:
        return [number for number in numbers_list if number % 2 != True]
    if filter == PRIME:
        return [number for number in numbers_list if is_prime(number)]