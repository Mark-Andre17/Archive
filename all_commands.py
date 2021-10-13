from config import documents, directories


def get_people(doc_number):
    for name_number in documents:
        if doc_number in name_number['number']:
            print("Вас зовут: ", name_number['name'])


def get_shelf(doc_number):
    shelf_break = False
    for directory in directories.items():
        for shelf in directory[1]:
            if doc_number == shelf:
                print("Номер полки: ", directory[0])
                shelf_break = True
                break
        if shelf_break:
            break
    else:
        print("Такой полки не существует!")


def people_list():
    for people in documents:
        print(people["type"], '"' + people["number"] + '"', '"' + people["name"] + '"' + ";")


def add_document(type_1, number_1, name_1, directory_1):
    documents.append({"type": type_1, "number": number_1, "name": name_1})
    print("Ваши данные добавлены в архив: ", "\n", documents)
    if directory_1 in directories.keys():
        directories[directory_1].append(number_1)
        print("Ваши данные добавлены на полку: ", "\n", directories)
    else:
        print("\n", "Данного номера полки не существует.")


def del_document(doc_number):
    break_number = False
    for document in documents:
        if document['number'] == doc_number:
            documents.remove(document)
            for directory_value in directories.values():
                if doc_number in directory_value:
                    directory_value.remove(doc_number)
                    print("Документ удален из архива и с полки.", "\n", documents, "\n", directories)
                    break_number = True
                    break
            if break_number:
                break
    else:
        print("\n", "Данный документ отсутствует!")


def move_document():
    break_doc = False
    doc_number = input("Введите номер документа: ")
    for value in directories.values():
        if doc_number in value:
            break_doc = True
            shelf_number = input("Введите полку на которую хотите переместить документ: ")
            for key in directories.keys():
                if shelf_number in key:
                    value.remove(doc_number)
                    directories[shelf_number].append(doc_number)
                    print("Документ перемещен")
                    print(directories)
                    break
            else:
                print("Такой полки нет")
                break
            if break_doc:
                break
    else:
        print("Документ не найден!")


def add_shelf(shelf_num):
    for number_shelf in directories.keys():
        if shelf_num in number_shelf:
            print("Полка с таким номером уже существует")
            break
    else:
        directories[shelf_num] = []
        print(directories)