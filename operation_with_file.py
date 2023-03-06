from os import remove, rename


# Запись строки в файл
def note(text):
    with open('notice.csv', 'a') as file:
        file.write(f"{text} \n")


# Чтение списка заметок
def read_notes():
    i = 0
    with open('notice.csv', 'r') as file:
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
    with open('notice.csv', 'r') as file:
        lines = file.read().strip().split("\n")
        for line in lines:
            i += 1
            if line == lines[index]:
                print(f"{i} | {line}")


# Выборка по дате
def read_notes_data(data):
    i = 0
    is_true = False
    with open('notice.csv', 'r') as file:
        while True:
            i += 1
            line = file.readline()
            if not line:
                break
            if data in line:
                print(f"{i} | {line}")
                is_true = True
        if not is_true:
            print("Заметка не найдена!")


# Изменение заметки
def replace_note(index, new_line):
    index -= 1
    with open('notice.csv', 'r') as file1, \
            open('noticetmp.csv', 'a') as file2:
        lines = file1.read().strip().split("\n")
        lines[index] = new_line
        for line in lines:
            file2.write(f"{line}\n")
    print("Заметка изменена успешно!")
    remove('notice.csv')
    rename('noticetmp.csv', 'notice.csv')


# Удаление заметки
def remove_note(index):
    index -= 1
    with open('notice.csv', 'r') as file1, \
            open('noticetmp.csv', 'a') as file2:
        lines = file1.read().strip().split("\n")
        for line in lines:
            if line != lines[index]:
                file2.write(f"{line}\n")
    print("Заметка удалена успешно!")
    remove('notice.csv')
    rename('noticetmp.csv', 'notice.csv')
