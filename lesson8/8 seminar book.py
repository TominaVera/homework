 



















def work_with_phonebook():
	

    choice=show_menu()

    phone_book=read_txt('phonebook.csv')

    while (choice!=7):

        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('lastname ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            last_name=input('lastname ')
            new_number=input('new  number ')
            print(change_number(phone_book,last_name,new_number))
        elif choice==4:
            lastname=input('lastname ')
            print(delete_by_lastname(phone_book,lastname))
        elif choice==5:
            
            print(write_txt('phone_book.txt',phone_book))
        elif choice==6:
            add_user(phone_book)
            


        choice=show_menu()

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Поменять номер телефона абонента\n"
          "4. Удалить абонента из справочника\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Добавить абонента в справочник\n"
          "7. Закончить работу")
    choice = int(input())
    return choice

def read_txt(filename): 

    phone_book=[]

    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.replace('\n', '').split(',')))
            phone_book.append(record)	
    return phone_book

def print_result(phone_book):
    for record in phone_book:
        print(record)

def find_by_lastname(phone_book,last_name):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            return(record)
    return('Ничего не найдено')


def write_txt(filename , phone_book):

    with open(filename,'w' ,encoding='utf-8') as phout:

        for i in range(len(phone_book)):

            s='' 
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}\n')
    return('Файл записан')

def change_number(phone_book,last_name,new_number):
    for i in range(len(phone_book)):
        if phone_book[i]['Фамилия'] == last_name:
            phone_book[i]['Телефон'] = new_number
            write_txt('phonebook.csv',phone_book)
            return('Номер изменен')
def delete_by_lastname(phone_book,lastname):
    for i in range(len(phone_book)):
        if phone_book[i]['Фамилия'] == lastname:
            phone_book.pop(i)
            write_txt('phonebook.csv',phone_book)
            return('Пользователь удален')
    return('Пользователь не найден')

def add_user(phone_book):
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    values = []
    for i in fields:
        values.append(input(i+' '))
    record = dict(zip(fields, values))
    phone_book.append(record)	
    write_txt('phonebook.csv',phone_book)
    return('Добавили нового абонента')


work_with_phonebook()



























