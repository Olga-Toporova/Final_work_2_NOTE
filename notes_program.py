from sys import exit
from exceptions import check_line, check_file
from input_data import input_index, input_text, input_data, choice_operation
from operation_with_file import read_notes, read_notes_ind, read_notes_data, replace_note, note, remove_note


def menu():
    print("1 - создать заметку\n"
          "2 - редактировать заметку\n"
          "3 - удалить заметку\n"
          "4 - вывести список заметок\n"
          "5 - вывести заметки по дате\n"
          "6 - вывести заметку по номеру\n"
          "0 - выход")
    operation(choice_operation())


# Выбор действий
def operation(choice):
    if choice == "0":
        print("Выход из программы, до свидания!")
        exit(0)
    if choice == "1":
        note(input_text())
    if choice == "2":
        index = input_index()
        if check_file() == True and check_line(index) == True:
            replace_note(index, input_text())
    if choice == "3":
        index = input_index()
        if check_file() == True and check_line(index) == True:
            remove_note(index)
    if choice == "4":
        if check_file() == True:
            read_notes()
    if choice == "5":
        if check_file() == True:
            read_notes_data(input_data())
    if choice == "6":
        index = input_index()
        if check_file() == True and check_line(index) == True:
            read_notes_ind(index)
    menu()


print("Добро пожаловать!")
menu()
