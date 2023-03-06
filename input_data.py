from datetime import datetime


# Выбор действия
def choice_operation():
    while True:
        try:
            choice = input("Выберите опцию: ")
            if choice.isdigit and int(choice) in range(0, 7):
                return choice
            else:
                print("Некорректный ввод, значение вне диапазона 0-6")
        except ValueError:
            print("Неверное значение, попробуйте еще раз.")


# Ввод текста заметки
def input_text():
    dt = datetime.now().strftime('%Y-%m-%d | %H:%M')
    return f"{dt} | {input('Введите заголовок заметки (Enter - завершение ввода): ').upper()} | {input('Введите текст заметки (Enter - завершение ввода): ')}"


# Ввод номера строки для операций поиска
def input_index():
    while True:
        try:
            line_index = input("Введите номер строки: ")
            if line_index.isdigit:
                return int(line_index)
            else:
                print("Некорректный ввод, попробуйте снова")
        except ValueError:
            print("Неверное значение, попробуйте еще раз.")


def input_data():
    while True:
        try:
            d = input("Введите интересующую дату в формате гггг-мм-дд: ")
            form = '%Y-%m-%d'
            res = bool(datetime.strptime(d, form))
            if res == True:
                return d
            else:
                print("Некорректный ввод, попробуйте снова")
        except ValueError:
            print("Неверное значение, попробуйте еще раз.")
