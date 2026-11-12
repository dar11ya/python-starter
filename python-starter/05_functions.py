# Функції: аргументи, return, область видимості, lambda, рекурсія

# ФУНКЦІЯ
# Це об'єкт, який приймає та повертає значення. Допомагає уникнути повторення в коді

def print_sum():
    print(2+2)

# print_sum()

def example():
    pass #заглушка

def example2():
    ... #заглушка 2

def example3():
    """Docstring for information""" #заглушка

# print(help(example3))
# def print_sum1(a, b):
#     print(a + b)
#
# print_sum1(1, 3)
#
# def printing_positional_arguments(first, second, *THIRD):
#     print(f"{first=} and {second=}, {THIRD=}")
#
# printing_positional_arguments('FIRST', 'SECOND', 'THIRD', 'FIRST', 'SECOND', 'THIRD')

# def print_sum(a, b, *elements):
#     print(a + b + sum(elements))
#
# print_sum(1, 2, 3, 4, 5, 6, 7)

# ключові аргументи
# def printing_positional_arguments(first, second, third):
#     print(f"{first=} and {second=}, {third=}")
#
# printing_positional_arguments(first='FIRST', second='SECOND', third='THIRD')

# **kwargs - сюда запаковуються додаткові параметри у словник
# def hello_user(job_position, name, surname, middlename=" ", **kwargs):
#     print(f"Hello {name} {surname} {middlename} your job position is {job_position}")
#
# hello_user("programmer", name="Mark", surname="Dil", your_country="Brazil")

# def sum_two_numbers(a, b):
#     print(1+3)
#     return 1+2
#
# result = sum_two_numbers(3, 5)
# print(result)

# Знайдіть максимальне значення в списку, що передається в функцію, і поверніть його, якщо воно більше 0
# в іншому випадку поверніть повідомлення про те, що число менше 0

# def finding_the_max_value_in_list(numbers_list):
#     result = 0
#     for e in numbers_list:
#         if e > result:
#             result = e
#
#     if result <= 0:
#         return "number less than 0 or equal"
#     else:
#         return result
#
# max_value_from_list = finding_the_max_value_in_list([4, 5, 3, 5, 6, 0, 1, 2])
# print(max_value_from_list)

# def finding_the_max_value_in_list(numbers_list):
#     result = 0
#     for e in numbers_list:
#         if e > result:
#             result = e
#     return "number less than 0 or equal" if result <= 0 else result
#
# max_value_from_list = finding_the_max_value_in_list([4, 5, 3, 5, 6, 0, 1, 2])
# print(max_value_from_list)
#

# def finding_the_max_value_in_list(numbers_list):
#     result = max(numbers_list)
#     return "number less than 0 or equal" if result <= 0 else result
#
# max_value_from_list = finding_the_max_value_in_list([4, 5, 3, 5, 6, 0, 1, 2])
# print(max_value_from_list)

# Поверніть кількість літер у слові, яке надсилається у параметрах.
# def counting_letters(word):
#     return len(word)
#
#
# number_letter = counting_letters('hello')
# print(number_letter)

#Напишіть функцію, яка зводить до ступеня число, яке передається у параметрах, якщо ступінь не є негативним.
# Перший параметр - число, другий - ступінь, у якого його необхідно звести.

# def exponentiate_number(number, power):
#     if power > 0:
#         return number**power
#     else:
#         return number
#
# print(exponentiate_number(2, 3))
#
# def exponentiate_number(number, power):
#     if power > 0:
#         return pow(number, power)
#     return number
#
# print(exponentiate_number(2, 3))


"""Завдання 1
Написати функцію, яка приймає 2 аргументи – цілих числа. Усередині функції робиться перевірка
типу. Якщо хоча б одне з них не int, то повертається 1, якщо обидва int, то вважається їхня сума.
Якщо сума позитивна, повертається 0, якщо негативна, то -1."""
# def type_check(first_arg, second_arg):
#     if type(first_arg) != int or type(second_arg) != int:
#         return 1
#     if type(first_arg) == int and type(second_arg) == int:
#         return first_arg + second_arg
#
# checking_value_type = type_check(10, 5)
# print(checking_value_type)

"""Завдання 2
Написати функцію, яку передається аргументом інша функція. Всередині приймаючої функції
зробіть виведення в консоль “Початок дзвінка”, після чого викличте функцію та результат
виведіть у консоль, після чого виведіть у консоль “Кінець дзвінка”. Для прикладу можете
написати функцію додавання 2 чисел і передати її в приймаючу функцію."""

# def accepting_function(calling_function):
#     print("Початок дзвінка")
#
#     result = calling_function()
#     print(result)
#
#     print("Кінець дзвінка")
#
# accepting_function(example)

# ОБЛАСТЬ ВИДИМОСТІ ФУНКЦІЇ
# Є ГЛОБАЛЬНІ ТА ЛОКАЛЬНІ
# ЗМІННІ ОГОЛОШЕННІ ПОЗА МЕЖАМИ ФУНКЦІЇ НАЗИВАЮТЬ ГЛОБАЛЬНИМИ
# x = 1 # глобальна змінна
# def print_x():
#     print(x)
#
# print_x()
#
# def print_local_y():
#     y = 1
#     print(y)
#
# print_local_y()

# Все що створюється всередині функції - доступно тільки всередині функції
# def external():
#     """LEGB enclosed"""
#     x = 1
#     def internal():
#         return x
#     return internal()
#
# print(external())
# product = 'bread'
#
# def changing_product():
#     product = 'Milk'
#     print("local: ", product)
#
#     def showing_enclosed():
#         # nonlocal product
#         global product
#         #print('Inside showing enclosed', product)
#         product = 'Cola'
#         print("Enclosed scope: ", product)
#
#     showing_enclosed()
#
#     print(product, '-----')
#
# changing_product()
#
# print('Global: ', product)

# Анонімні функції - використовуються у випадку, якщо нам їх потрібно кудись передати і більше ми їх не юудемо
# використовувати повторно

# lambda
# def foo():
#     return 1
#
# l = lambda x: x
#
#
# print(l.__name__)
# print(foo.__name__)
#
# def power(x, y):
#     return x ** y
#
# print(power(2, 8))
#
# p = lambda x, y: x ** y
# print(p(2, 8))
#
# n = [1, 3, 5, 14, 6, 7, 8,]
# n.sort(key=lambda x: -x)
# print(n)
#
# z = list(map(lambda elem: elem**2, n))
# print(z)

# Напишіть функцію,де дано натуральне число n. Виведіть усі числа від 1 до n

# def printing_numbers_till_n(n) -> None:
#     if n >= 1:
#         printing_numbers_till_n(n - 1)
#         print(n)
#
# printing_numbers_till_n(15)

# Напишіть функцію для прорахунку площі прямокутника, у параметраї передається висота та довжина
# def rectangle_area(n, l) -> Int:
#     return n * l
#
# print(rectangle_area(4, 3))
# rectangle_area_l = lambda n, l: n * l
# print(rectangle_area_l(4, 3))

# # Напишіть функцію, яка змінює значення глобальної змінної
# global_var = 12
#
# def changing_global_var_value():
#     global global_var
#     global_var = 14
#
# changing_global_var_value()
# print(global_var)

# Напишіть рекурсивну функцію для того, щоб порахувати значення факторіалу числа, що
# передається аргументом (див. рекомендовані ресурси).

# def counting_factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * counting_factorial(n-1)
#
# print(counting_factorial(5))
