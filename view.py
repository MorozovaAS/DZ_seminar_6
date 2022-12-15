def action ():
    print("Если хотите найти телефон нажмите 1, \nЕсли хотите ввести новый контакт нажмите 2: ")
    result = input()
    return result

def new_contact():
    result = input("Введите ФИО и телефон: ")
    return result

def cont_to_search():
    result = input("Введите данные для поиска: ")
    return result