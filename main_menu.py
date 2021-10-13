from help_menu import help_menu
from all_commands import get_people, get_shelf, people_list, add_document, del_document, move_document, add_shelf


def main_menu():
    help_menu()
    while True:
        menu_command = input("Введите команду:/ ")
        if menu_command == "p":
            get_people(doc_number=input('Введите номер документа: '))
        elif menu_command == "h":
            help_menu()
        elif menu_command == "s":
            get_shelf(doc_number=input('Введите номер документа: '))
        elif menu_command == "l":
            people_list()
        elif menu_command == "a":
            add_document(type_1=input("Введите тип документа на английском языке: "),
                         number_1=input("Введите номер документа: "),
                         name_1=input("Введите имя и фамилию: "),
                         directory_1=input("Введите номер полки,в которую хотите поместить документ: "))
        elif menu_command == "d":
            del_document(doc_number=input('Введите номер документа: '))
        elif menu_command == "m":
            move_document()
        elif menu_command == "as":
            add_shelf(shelf_num=input("Введите номер новой полки: "))
        elif menu_command == "q":
            print("Прощайте!")
            break
        else:
            print("Команда введена неправильно. Попробуйте еще раз")
    else:
        False
