#Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.


# import collections
# cntr = collections.Counter([33, 24, 3, 3, 4, 4, 2])  
# print(*filter(lambda x: cntr[x] == 1, cntr.keys()))  


# Задание
# Формат: На семинаре и в лекциях мы разобрали новые функции, которые позволяют улучшить код прошлых задач.
# Задача: предложить улучшения кода для уже решённых задач(не менее 4 задач нужно улучшить):
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# В этом случае можно пропустить совсем тривиальные (т.е. задачу 1 или 2 тут точно решать не имеет смысла) - исходите из уровня группы и студента.


# Написать программу, которая считает буквы слов в списке.
# lst = ["Берлин", "Амстердам", "Москва", "Денвер", "Токио"]
# b = map(len, lst)
# a = list(b)
# print(a)

#Написать программу, которая попарно соединяет элементы списка.
# words = ['a', 'b', 'c', 'd', 'e']
# numbers = [1,2,3,4,5]
# results = list(zip(words, numbers))
# print(results)

#Дан список чисел. Написать программу, которая выведет только те числа, которые больше заданного числа.

# lst = [32, 90, 71, 9, 44, 60, 95, 100, 81, 65]
# def List_numbers(nums):
#     return nums > 10
# over = list(filter(List_numbers, lst))
# print(over)

# Дан список. Написать программу, которая выведет только палиндромные значения.

# lst = ("fghgf", "dfgs", "alkla", "freer", "ertrth", "12321")
# palindromes = list(filter(lambda word: word == word[::-1], lst))
# print(palindromes)

#Найти сумму всех элементах которые находятся на нечетных позициях.

# numbers = [10, 5, 20, 34, 40, 60, 70, 80]
# sum = 0
# for index, number in enumerate(numbers, 1):
#  if index % 2 == 0:
#     sum += number
# print(sum)
