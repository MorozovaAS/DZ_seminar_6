def new_entry(result):
    with open('phonebook.txt', 'a', encoding='utf-8') as data:
        data.write(f'{str(result)}\n')

import codecs
def get_data():    #получить данные
   f = codecs.open('phonebook.txt', 'r', "utf_8_sig")
   return f



