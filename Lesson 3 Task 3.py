"""Homework 3 Task 3

    3. Реализовать функцию my_func(),
    которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

    """


def my_func(var_1, var_2, var_3):
    return var_1 + var_2 + var_3 - min(var_1, var_2, var_3)


print(my_func(110, 300, 90))
