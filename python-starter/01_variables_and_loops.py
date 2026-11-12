# Змінні, рядки, цикли while/for, break/continue

# # Напишіть програму, використовуючи знання про змінні типу цілих чисел, щоб порахувати за який
# # час транспортний засіб доїде з пункту А до пункту В, якщо відомі такі дані: відстань від А до В =
# # 250 км, швидкість автомобіля буде постійною та дорівнює 80 км/год. . Використовуйте формулу:
# # Час = відстань/швидкість. Створіть змінні length, куди запишіть відстань, velocity, куди запишіть
# # швидкість та змінну time, куди запишіть результат. Після цього використовуйте метод print(), щоб
# # вивести в консоль результат.
# from unittest import result
#
# # length = 250
# # velocity = 80
# # time = length/velocity
# # print(f'Автомобіль проїде {length}км зі швидкістю {velocity}км.год за {time}')
#
# # Створіть змінну age = 25, змінну name = "John". Виведіть у консоль “My name is
# # <name> and I am <age>”, але зробіть рішення таким, щоб використовувалася конкатенація рядків
# # (через +) та приведення типу числа до рядка (str(...)). Тобто, щоб замінити змінні age і name, то методі
# # print() нічого не потрібно було змінювати. Наприклад, a = 10, print(“Value =” + str(a)) і буде “Value =
# # 10”
#
# # age = 25
# # name = "John"
# # print("My name is ",  name, "and I am " + str(age) + " years old.")
#
# # counter = 5
# # while counter > 0:
# #     counter -= 1
# #
# # print(counter)
#
# # counter = 10
# # while True:
# #     counter -= 1
# #     print(counter)
# #     if counter == 5:
# #         break
# #         print("Text after break")
#
# # counter = 0
# # while counter < 10:
# #     counter += 1
# #     if(counter % 2) == 0:
# #         continue
# #     print(counter)
#
# #
# # for e in range(4):
# #     if e == 1:
# #         break
# #     print(e)
#
# # Пройтися по списку від 0 до 101 і надрукувати тільки парні
#
# # for i in range(102):
# #     if i == 0 and i % 2 == 0:
# #         print(i)
# #
#
# # Пройтися по слову hello і замінити l на s
# # answer = ''
# # for e in "hello":
# #     if e == "l":
# #         answer += "s"
# #     else:
# #         answer += e
# #
# # print(answer)
#
# # Вивести у консоль перші 100 чисел Фібоначі
#
# # fibo_num = []
# #
# # for e in range(0,100):
# #     if e >= 2:
# #         e = fibo_num[-1] + fibo_num[-2]
# #         fibo_num.append(e)
# #     elif e == 0:
# #         fibo_num.append(1)
# #     elif e == 1:
# #         fibo_num.append(1)
# #
# # print(fibo_num)
#
# # У пропозиції “Hello world” замінити всі літери “o” на “a”, а літери “l” на “e”.
#
# # word = "Hello world".replace("o", "a")
# # print(word.replace("l", "e"))
#
# # word = "Hello world"
# # result = []
# # for letter in word:
# #     if letter == "o":
# #         result.append("a")
# #     elif letter == "l":
# #         result.append("e")
# #     else:
# #         result.append(letter)
# #
# # print(result)
#
# # Створіть будь-який змінний рядок і помістіть будь-який текст. Зробіть так, щоб усі непарні по
# # порядку ліворуч на право символи стали "_", а всі символи, розташування яких парне і які рівні
# # "a" - стали "b". Наприклад "Ham is tasty" => "_b_ _s_t_s_y".
#
# # first_str = "Ham is tasty"
# # result = []
# #
# # for (e, i) in enumerate(first_str):
# #     if e % 2 == 0:
# #         result.append("_")
# #     elif e % 2 == 1 and i == "a":
# #         result.append("b")
# #     else:
# #         result.append(i)
# #
# # print("".join(result))
#
# # Пройтись по діапазону чисел від 0 до 100 і вивести лише ті, які діляться на 3.
# # result = []
# #
# # for e in range(0, 101):
# #     if e % 3 == 0:
# #         result.append(e)
# #
# # print(result)
#
# # Пройтись по діапазону чисел від 0 до 100, виводити всі числа, при цьому пропустити число 4 і,
# # як тільки цикл досягне числа 18 - вийти з циклу.
#
# # result = []
# # for e in range(0, 101):
# #     if e == 4:
# #         continue
# #     if e == 18:
# #         break
# #     else:
# #         result.append(e)
# #
# # print(result)
