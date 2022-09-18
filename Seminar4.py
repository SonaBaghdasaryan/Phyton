#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# nums = int(input())
# i = 2
# while nums > 1:
#     while n % i == 0:
#         print(i, end=' ')
#         n //= i
#     i += 1

#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


# a = [int(s) for s in input().split()]
# for i in range(len(a)):
#     for j in range(len(a)):
#         if i != j and a[i] == a[j]:
#             break
#     else:
#         print(a[i], end=' ')


#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


# from solution import Polynomial
# poly1 = Polynomial([0, 0, 1])
# print(poly1(-2))
# print(poly1(-1))
# print(poly1(0))
# print(poly1(1))
# print(poly1(2))
# print()
# poly2 = Polynomial([0, 0, 2])
# print(poly2(-2))
# print(poly2(-1))
# print(poly2(0))
# print(poly2(1))
# print(poly2(2))
# print()
# poly3 = poly1 + poly2
# print(poly3(-2))
# print(poly3(-1))
# print(poly3(0))
# print(poly3(1))
# print(poly3(2))
# print()











 
