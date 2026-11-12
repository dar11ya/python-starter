# Списки: перебір, пошук максимуму, видалення елементів, паліндром

#
#
# # number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#
# # for number in number_list:
# #     if number % 2 == 0:
# #         number_list.remove(number)
# #     else:
# #         pass
# #
# # print(number_list)
# # index = 0
# # while True:
# #     if index < len(number_list):
# #         if number_list[index] % 2 == 0:
# #             number_list.remove(number_list[index])
# #         index += 1
# #     else:
# #         break
# # print(number_list)
#
# # Звести всі елементи списку у квадрат
# number_list_squares = list()
# #
# # for number in number_list:
# #     number_list_squares.append(number ** 2)
# #
# # print(number_list_squares)
#
# # for index in range(len(number_list)):
# #     number_list[index] = number_list[index] ** 2
# #
# # print(number_list)
#
# # Знайти макс елемент списку
# # number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# # index = 0
# # max_number = None
# #
# # while index < len(number_list) - 1:
# #         if number_list[index] > number_list[index + 1]:
# #             max_number = number_list[index]
# #         else:
# #             max_number = number_list[index + 1]
# #         index += 1
# #
# # print(max_number)
#
# # maximum = number_list[0]
# #
# # for e in range(len(number_list)):
# #     if number_list[e] > maximum:
# #         maximum = number_list[e]
# #
# # print(maximum)
#
# # print(max(number_list))
#
# # print(sorted(number_list) [-1])
#
# # number_list.sort()
# # print(number_list[-1])
#
# #  Є список а = [2, 4, 65, 32, 2, 6, 0, -1, 3]. Вивести всі значення менше 5 у консоль.
#
# # list1 = [2, 4, 65, 32, 2, 6, 0, -1, 3]
# # for el in list1:
# #     if el < 5:
# #         print(el)
#
# # # "aabbаа" - паліндром. Як це перевірити?
# # list1 = ['a', 'a', 'b', 'b', 'a', 'a']
# # first_part = list1[:3]
# # second_part = list1[3:]
# # index = 0
# # var = len(second_part) - 1
# #
# #
# #
# # while index < len(first_part) and var != -1:
# #     if first_part[index] == second_part[var]:
# #         print('Поки все сходиться')
# #     else:
# #         print('Щось не так')
# #     index += 1
# #     var -= 1
#
# # На основі списку a = ['red', 'yellow', 'blue', 'bread']
# # Створити список, у якому буде лише слово, зайве у списку a.
#
# # list1 = ['red', 'yellow', 'blue', 'bread']
# # list2 = []
# # list2.append(list1[-1])
# #
# # print(list2)
