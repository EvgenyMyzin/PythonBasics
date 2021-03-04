"""Homework 3 Task 4

    4. Программа принимает действительное положительное число x и целое отрицательное число y.
    Необходимо выполнить возведение числа x в степень y.
    Задание необходимо реализовать в виде функции my_func(x, y).
    При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

    Подсказка: попробуйте решить задачу двумя способами.
    Первый — возведение в степень с помощью оператора **.
    Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

    """


def my_func1(var_1, var_2):
    return var_1**var_2

def my_func2(var_1, var_2):
    power = 1 / var_1
    for power_count in range(1, abs(var_2)):
        power = power * (1 / var_1)
    return power


print(my_func1(1.5, -4))
print(my_func2(1.5, -4))
