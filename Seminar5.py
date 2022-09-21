#1 Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


# lst = ['впк', 'ыуапку', 'вапабв', 'фкак', 'абв']
# print(*filter(lambda x:not 'абв' in x, lst))




#2 Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""



# from random import randint, choice
# greeting = ('Здравствуйте! Вас приветствует игра "Забери все конфеты!" '
#             'Основные правила игры: '
#             'Нам будет дано некоторое количество конфет, '
#             'за один ход мы можем взять не более определённого количества, '
#             'о котором мы с вами договоримся. '
#             'Итак, начнём!')
# messages = ['Ваша очередь брать конфеты', 'возьмите конфеты',
#             'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']
# def introduce_players():
#     player1 = input('Давайте познакомися. Как Вас зовут?\n')
#     player2 = 'Робик'
#     print(f'Очень приятно, меня зовут {player2}')
#     return [player1, player2]
# def get_rules(players):
#     n = int(input('Сколько конфет будем разыгрывать?\n '))
#     m = int(input('Сколько максимально будем брать конфет за один ход?\n '))
#     first = int(input(
#         f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
#     if first != 1:
#         first = 0
#     return [n, m, int(first)]
# def play_game(rules, players, messages):
#     count = rules[2]
#     print(count)
#     if rules[0] % 10 == 1 and 9 > rules[0] > 10:
#         letter = 'а'
#     elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
#         letter = 'ы'
#     else:
#         letter = ''
#     while rules[0] > 0:
#         if not count % 2:
#             move = rules[0] % rules[1] + 1
#             print(f'Я забираю {move}')
#         else:
#             print(f'{players[0]}, {choice(messages)}')
#             move = int(input())
#             if move > rules[0] or move > rules[1]:
#                 print(
#                     f'Это слишком много, можно взять не более {rules[1]} конфет{letter}, у нас всего {rules[0]} конфет{letter}')
#                 attempt = 3
#                 while attempt > 0:
#                     if rules[0] >= move <= rules[1]:
#                         break
#                     print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
#                     move = int(input())
#                     attempt -= 1
#                 else:
#                     return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
#         rules[0] = rules[0] - move
#         if rules[0] > 0:
#             print(f'Осталось {rules[0]} конфет{letter}')
#         else:
#             print('Все конфеты разобраны.')
#         count += 1
#     return players[not count % 2]


# print(greeting)

# players = introduce_players()
# rules = get_rules(players)

# winer = play_game(rules, players, messages)
# if not winer:
#     print('У нас нет победителя.')
# else:
#     print(
#         f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')

#3 Создайте программу для игры в ""Крестики-нолики""
from tkinter import *
 
window = Tk()
window.geometry('360x360')
window.title('Крестики и нолики')
 
w = 120
xod = 0
Button_list = []
kre_num = []
li_way = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
class Btn():
    global w, Button_list
    def __init__(self,x0,y0,idd):
        self.idd = idd
        self.x0 = x0
        self.y0 = y0
        self.Button1 = Button(bg = 'green',bd = 10, fg = 'white', font = ('Comic Sans MS', 24, 'bold'))
        self.Button1.place(x = self.x0,y = self.y0,width = w, height = w)
        self.Button1.bind('<Button-1>',self.click)
    def unbind1(self,event):
        self.Button1.unbind('<Button-1>')
    def cfg(self):
        self.Button1.config(fg = 'blue')
    def show(self):
        idd = 0
        x = 0
        y = 0
        for i in range(3):
            for j in range(3):
                Button_list.append(Btn(x,y,idd))
                x += w
                idd += 1
            x = 0
            y += w
    def click(self, event):
        print(self.idd)
        global xod, li_way, kre_num
        win = False
        if xod % 2 == 0:
            char = 'X'
            kre_num.append(self.idd)
        else:
            char = '0'
        self.Button1.config(text=char)
        xod += 1
        #Проверка
        k = 0
        for i in range(8):
            for j in range(3):
                if li_way[i][j] in kre_num:
                    k+=1
            if k ==3:
                print('norm')
                win = True
                break
            else:
                k = 0
        self.Button1.unbind('<Button-1>')
        if win:
            for g in range(9):
                Button_list[g].unbind1('<Button-1>')
            for g in range(3):
                Button_list[li_way[i][g]].cfg()
 
        
Btn.show(0)
window.mainloop()

#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# def rle(str):
#     result = []
#     count = 0
 
#     if len(str) == 1:
#         result.append((1, int(str[0])))
#         return result
 
#     for i in range(len(str)):
#         count += 1
#         if (i + 1) == len(str) or str[i] != str[i + 1]:
#             result.append((count, int(str[i])))
#             count = 0
            
#     return result
 
# if __name__ == "__main__":
 
#     str = input()
#     result = rle(str)
 
#     for amount, figure in result:
#         print(amount, figure)
 
