# Множини та кортежі

# МНОЖИНИ І КОРТЕЖІ
# Множини - це структура даних, що не містить елементів, що повторюються. Не мають індексацію

# Перший спосіб створення множини
some_set = {'a', 'b', 'c', 'c'} # a, b, c

# Другий спосіб створення множини
some_set1 = set(['a', 'b', 'c'])

# колекції (список, рядок, словник, множина, кортежі)
# print(len(some_set)) # 3
# print('a' in some_set) #true

# В множину можна вставляти лише незмінні елементи
# frozenset - це незмінний об'єкт, який не можна редагувати
some_frozen_set = frozenset(['a', 'b', 'c'])

# МЕТОДИ
# clear() - очищає множину
# pop() - видаляє елемент множини і повертає будь-який елемент
# some_set.clear()
# print(some_set.pop())

# discard(elem) - видаляє елемент із множини
# remove(elem) - видаляє елемент із множини. Якщо такого елемента немає, видає помилку
# add(elem) - додає елемент у множину
# union(another_set) - поєднує множини
# intersection(another_set) - знаходить перетин множин
some_set_products = {"bread", "cheese", 'a', 'b', "milk", "eggs"}
# print(some_set.union(some_set_products))
# print(some_set | some_set_products) # те саме що union
# print(some_set =| some_set_products) #робить те саме, але не повертає нову множину, а змінює першу
# print(some_set.intersection(some_set_products))
# print(some_set & some_set_products ) #той самий результат на перетин

# difference(another_set) - різниця між множинами
# elem in set_name - чи знаходиться елемент у множині

# print(some_set.isdisjoint(some_set_products)) #повертає bool що немає спільних елементів у цих множинах
# print(some_set.issubset(some_set_products)) #перевірка, що всі елементи some_set є елементами множини some_set_products
# print({1, 2, 3} <= {1, 2, 3, 4}) # те саме що issubset

#symmetric_difference() - створення нової множини яка є симетричною різницею цих множин
# print({1, 2, 3}.symmetric_difference({1, 2, 3, 4}))
# print({1, 2, 3} ^ ({1, 2, 3, 4})) # те саме що symetric_difference()

# КОРТЕЖ(TUPLE) - Це постійний перелік
# Синтаксис: (1, 2, 3) (1,)
# Якщо треба створити список що не змінний, наприклад пори року
# Всередині може збегатись любий тип

some_tuple = (1, 2, 3)
# print(some_tuple)

some_tuple1 = ([],  {}, set(), ())
# print(some_tuple1)

some_tuple2 = tuple(['a', 'b', 'c'])
# print(some_tuple2)

some_tuple3 = tuple("Hello I am python developer")
# print(some_tuple3)

#empty tuple
empty_tuple = ()
empty_tuple1 = tuple()

# Методів у кортежів тільки два - count(), index()
# print(len(some_tuple3)) #27
# print("H" in some_tuple3) #true
# print(some_tuple3.count('l'), 'count')
# print(some_tuple3.index('l'), 'index')

a, b, c = (1, 2, 3)
# print(a, b, c)

# свапінг двох змінних
a = 1
b = 2
c = a
a = b
b = c
del c
# print(a, b)

a, b = b, a #a = 2, b = 1'

# a, b, *anything = (b, a, c, 1, 3, 4, 'Hello') #a=2, b=1, anything=c, 1, 2,3, "hello"

# first, *middle, last = ("Igor", 'Mark', 'Lena', "Nazar")

class_school = (("Igor", 10), ('Mark', 12), ('Lena', 8), ("Nazar", 11))
# for s, mark in class_school:
    # print(f"Student: {s}, mark: {mark}")

# Є 2 множини A = {3, 5, 11, 7, 4 -3}, B = {11, 5, 8, 1, 10, 7}
# Завдання 1
# Вивести в консоль елементи A, яких немає в B.
A = {3, 5, 11, 7, 4, -3}
B = {11, 5, 8, 1, 10, 7}
# print(A.difference(B))
# print(A - B)


# Завдання 2
# Вивести в консоль загальні елементи А та В.
# print(A.intersection(B))
# print(A & B)

# Завдання 3
# Вивести в консоль об'єднання множин А та В.
# print(A.union(B))
# print(A | B)

# Завдання 4
# Чи є рядок a = “a14b6fh”, як дізнатися, що всі символи унікальні, використовуючи множини та
# списки?

# a = "a14b6fh"
# try_set = set(a)
#
# if len(try_set) == len(a):
#     print("yes")
# else:
#     print("no")
