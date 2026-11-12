# Винятки та їх обробка: try/except, raise, власні помилки

# ВИНЯТКИ ТА ЇХ ОБРОБКА
# винятки - це механізм обробки свідомо помилок та інших можливих проблем під час виконання програми
# помилок є три типи: синтаксичні, runtime, логічні помилки
# синтаксичні - наприклад написати print 'hello'
# runtime error - під час виконання коду, наприклад 1/0
# логічні помилки - найважкіші, бо можуть спрацювати, але неправильно
# для обробки винятків використовується блок try-except

# print('first step')
# try:
#     1/0
# except ZeroDivisionError:
#     print("You couldn't divide by zero")
#
# print('second step')
#
# def devide_two_numbers(first, second):
#     try:
#         answer = first / second
#     except ZeroDivisionError:
#         return "You couldn't divide by zero"
#     except (TypeError, Exception):
#         return "You didn't enter a number"
#     else: print('ok')
#     # finally:
#     #     return 'FINALLY'
#
#     return answer
#
# print(devide_two_numbers(1, 'str'))
#
# def bool_return():
#     try:
#         return True
#     finally:
#         return False
#
# print(bool_return())

# try:
#     raise ZeroDivisionError
# except:
#     print("I catch an error")

# assert - під капотом перевіряє елементи між собою і якщо вони не дорівнюють одне одному - піднімає помилку

# Реалізувати функцію, яка прийматиме на вхід номер місяця, повернути його разву та реалізувати в ньому кілька
# обробок винятків.
#
# def month_return(month_number):
#     months = ['January', 'February', 'March', 'April',
#               'May', 'June', 'July', 'August',
#               'September', 'October', 'November',
#               'December']
#
#     try:
#         month_index = abs(month_number) - 1
#         return months[month_index]
#     except TypeError:
#         return 'Please use only integers'
#     except IndexError:
#         return 'Please use integer between 1 and 12'
#
#
#
# print(month_return(12))
#
# assert month_return(1) == 'January'

# Потрібно перевірити, чи всі числа в послідосності є унікалььними і реалізувати кілька обробок винятків

def list_check_for_unique_numbers(any_list):
    try:
        return len(any_list[:]) == len(set(any_list))
    except TypeError as e:
        return f"Type error need to use only sequence type(str, list, range, tuple) \n Error {e} "

# print(list_check_for_unique_numbers([1, 3, 4, 5, 6, 7]))

class TurnOffLightError(Exception):
    def __str__(self):
        return 'You forgot to turn off the light!'

try:
    raise TurnOffLightError()
except TurnOffLightError as e:
    print(f'Error: {e}')
