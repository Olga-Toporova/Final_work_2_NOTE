from os import remove, rename


# Запись строки в файл
def note(text):
    with open('notice.txt', 'a', encoding='utf-8') as file:
        file.write(text)


# Чтение списка заметок
def read_notes():
    i = 0
    with open('notice.txt', 'r', encoding='utf-8') as file:
        while True:
            i += 1
            line = file.readline()
            if not line:
                break
            print(f"{i} | {line}")


# Чтение выбранной заметки
def read_notes_ind(index):
    index -= 1
    i = 0
    with open('notice.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            i += 1
            if line == lines[index]:
                print(f"{i} | {line}")


# Выборка по дате
def read_notes_data(data):
    i = 0
    with open('notice.txt', 'r', encoding='utf-8') as file:
        while True:
            i += 1
            line = file.readline()
            if not line:
                break
            if data in line:
                print(f"{i} | {line}")
            else:
                print("Заметка не найдена.")


# Изменение заметки
def replace_note(index, new_line):
    index -= 1
    with open('notice.txt', 'r', encoding='utf-8') as file1, \
            open('noticetmp.txt', 'a', encoding='utf-8') as file2:
        lines = file1.readlines()
        lines[index] = new_line
        for line in lines:
            file2.write(line)
    print("Заметка изменена успешно!")
    remove('notice.txt')
    rename('noticetmp.txt', 'notice.txt')


# Удаление заметки
def remove_note(index):
    index -= 1
    with open('notice.txt', 'r', encoding='utf-8') as file1, \
            open('noticetmp.txt', 'a', encoding='utf-8') as file2:
        lines = file1.readlines()
        for line in lines:
            if line != lines[index]:
                file2.write(line)
    print("Заметка удалена успешно!")
    remove('notice.txt')
    rename('noticetmp.txt', 'notice.txt')
