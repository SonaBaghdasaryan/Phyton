#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# from random import randint
# array = [randint(1,5) for _ in range(10)]            
# sum_ = 0
# for i,x in enumerate(array):
#     print("a[{}] = {}".format(i, x))
#     if i % 2 != 0:
#         sum_ += x
# print("Summ is = {}".format(sum_))




#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


# a = [2, 3, 4, 5, 6]
# n = len(a)
# if n > 1:
#     for i in range(n):
#         print(a[i] * a[n-1], end=' ')
# else:
#     print(*a)




#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


# n = int(input('Input the number: '))
# b = ' ' 
# while n > 0:
#   b = str(n % 2) + b
#   n = n // 2 
# print(b)



#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


# def fib(n: int) -> list:
#     if n == 1:
#         return [1]
#     elif n == 2:
#         return [1, 1]

#     lst = fib(n-1)
#     lst.append(lst[-1] + lst[-2])
#     return lst

# print(fib(8))
