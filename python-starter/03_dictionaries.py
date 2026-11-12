# Словники: створення, методи, підрахунок елементів

#
# # СЛОВНИКИ
# example_dict = {'key': 'value'}
# # print(example_dict.get('key')) #Інколи краще використати get, бо якщо такого ключа не існує get поверне None і не зафейлиться
#
# # варіант 1 побудови словника
# capital_cities = {
#     'Venezuela': 'Caracas',
#     'Nicaragua': 'Managua'
# }
#
# # варіант 2 побудови слованика
# capital_cities_2 = dict([['Venezuela', 'Caracas'], ['Nicaragua', 'Managua']])
# # print(capital_cities_2)
#
# # варіант 3 побудови словника, не можна щоб ключ був int
# capital_cities_2 = dict(Venezuela = 'Caracas', Nicaragua = 'Managua')
# # print(capital_cities_2)
#
# capital_cities['Ukraine'] = 'Kyiv'
# # print(capital_cities['Ukraine'])
# # print(capital_cities)
#
# # empty dictionary
# cities_year_foundation = {}
# cities_year_foundation = dict()
# cities_year_foundation['Kharkiv'] = 1654
# cities_year_foundation['Chuhuiv'] = 1638
#
# cities_year_foundation['Kharkiv'] = {'Year of foundation': 1654, 'Main rivers': ['Kharkiv', 'Lopan']}
# # print(cities_year_foundation)
#
# # HOW TO DELETE VALUE?
# del cities_year_foundation['Chuhuiv']
# # print(cities_year_foundation)
#
# # FOR WITH DICTIONARIES
# # print(capital_cities)
# for country in capital_cities:
#     # print(country, capital_cities[country])
#
# # items() - повертає пару: ключ, значення
# # for country, capital in capital_cities.items():
# #     print(country, capital)
#
# # clear() - Очищає словник
# # print(capital_cities)
# # capital_cities.clear()
# # print(capital_cities)
#
# # pop() - видаляє ключ і повертає відповідне значення
# # print(capital_cities.pop('Nicaragua'))
#
# # popitem() - видаляє останнє значення і повертає його у форматі ключ-значення
# # print(capital_cities.popitem())
#
# # update({'key': 'value'}) - додає нове ключ-значення
# capital_cities.update({'Brazil': 'Brazilia'})
# # print(capital_cities)
#
# malazia = {'Malazia': 'Kuala-Lampur'}
# capital_cities.update(malazia)
# # print(capital_cities)
#
# # values - повертає всі значення у словнику
# values_of_capital_cities = capital_cities.values()
# # print(values_of_capital_cities)
#
# # keys - повертає всі ключі словника
# keys_of_capital_cities = capital_cities.keys()
# # print(keys_of_capital_cities)
#
# # setdefault - якщо значення немає, повертає те що знаходить на другому місці аргумента
# # print('GET', capital_cities.get('Romania')) #We don't have Romania
# # print('SETDEFAULT', capital_cities.setdefault('Romania', 'Bucharest'))
#
# # fromkeys() - повертає зовсім новий словник з ключами - значеннями, перший аргумент - список, другий - value, по замовчуванні None
# empty_dictionary = {}
# days_name_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',]
# empty_dictionary.fromkeys(days_name_list)
# # print(empty_dictionary)
#
# # Порахувати за допомогою словника скільки разів елемент повторюється у списку
classmate_name = ['Sergey', 'Igor', 'Tanya', 'Sergey', 'Machael', 'Sergey', 'Lena']
# answer = {}
# for name in classmate_name:
#     if name in answer.keys():
#         answer[name] += 1
#     else:
#         answer[name] = 1
#
# print(answer)
# v2
# answer = {}
#
# for name in classmate_name:
#     answer[name] = classmate_name.count(name)
#
# print(answer)

# # Пройтися за словником і вивести всі значення, які мають парний ключ
# data_dict = {22: 'one', 1: 'one', 33: 'any text', 5: 5, 6: '6', 9: '9'}
# for key, value in data_dict.items():
#     if key % 2 == 0:
#         print(value)

# # Видалити всі ключі, значення яких починається з літери
# only_int_keys = {1: 'value', 'key': 123, 2: 'value', 'key2': 123}
# only_int_keys_copy = only_int_keys.copy()
#
# for key in only_int_keys:
#     if type(key) == str:
#         del only_int_keys_copy[key]
#
# print(only_int_keys_copy)

# max_dict = {'a': 3, 'b': 'hello', 'c': 4, 'd': -3}
# max_value = next(iter(max_dict.values()))
#
# for value in max_dict.values():
#     if type(value) == int:
#         if value > max_value:
#           max_value = value
#
# print(max_value)
