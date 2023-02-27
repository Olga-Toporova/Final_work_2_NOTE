from os import path


# Проверка на наличие файла
def check_file():
    if path.exists('notice.txt'):
        return True
    else:
        print('Заметок нет, создайте заметку!\n')
        return False


# Наличие строки по индексу
def check_line(index):
    with open('notice.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if index > len(lines):
            print('Cтрока не найдена!')
            return False
        else:
            return True
