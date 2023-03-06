from os import path
import json


# Проверка на наличие файла
def check_file():
    if path.exists('notice.csv'):
        return True
    else:
        print('Заметок нет, создайте заметку!\n')
        return False


# Наличие строки по индексу
def check_line(index):
    with open('notice.csv', 'r') as file:
        lines = file.read().strip().split("\n")
        if index > len(lines):
            print('Cтрока не найдена!')
            return False
        else:
            return True
