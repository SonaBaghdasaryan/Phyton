#1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#Пример:
#- 6 -> да
#- 7 -> да
#- 1 -> нет

#day = int(input('Input the day of a week: '))
#if 1 <= day < 6:
    #print('No')
#else: print('Yes')

#2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# for x in range(2):
#   for y in range(2):
#     for z in range(2):
#       print(not (x or y or z) == (not x and not y and not z))


#3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = int(input('x = '))
# y = int(input('y = '))

# if x > 0 and y > 0:
#     print('1')
# elif x < 0 and y > 0:
#     print('2')
# elif x < 0 and y < 0:
#     print('3')
# else: print('4')

#4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# print('Input the number of quarter:')
# a = int(input())
# if a==1: print('x >0 and y > 0')
# elif a==3: print('x <0 and y < 0')
# elif a==4: print('x > 0 and y < 0')
# else: print('x > 0 and y < 0')

#5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# x1 = int(input("Input the coordinate of x1 : "))
# y1 = int(input("Input the coordinate of y1 : "))
# x2 = int(input("Input the coordinate of x2 : "))
# y2 = int(input("Input the coordinate of y2 : "))
# d = ((x2 - x1)**2 + (y2 - y1)**2)**(0.5)
# print(f"The distance is {d} ")
