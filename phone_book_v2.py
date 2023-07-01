class Field:
    def __init__(self, value):
        self.value = value


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def show_phones(self, name):
        if name in self.data.keys():
            for i,j in self.data.items():
                if name == i:
                    print(j.phones.data)
        else:
            print(f'No {name} in Address_book')

class Name(Field):
    def __str__(self):
        return self.value
    pass


class Phone(Field, UserList):
    def __init__(self, phone):
        self.data = [phone]
    def add_phones(self, phone):
        if self.data is None:
            self.data = []
        self.data.append(phone)
    pass


class Record(Field):
    def __init__(self, name, phone=None):
        self.name = name
        self.phones = phone


    def add_phone(self, phone):
        self.phones.add_phones(phone)


    def change_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone == old_phone:
                self.add_phone(new_phone)
                self.phones.remove(phone)
                return True

    def delete_phone(self, new_phone):
        for phone in self.phones:
            if phone == new_phone:
                self.phones.remove(phone)
                return True

def input_error(func):
    def inner(*args):
        try:  # Якщо виключення не сталося, то продовжуємо роботу 
            return func(*args)  # Викликаємо саму функцію handler  
        except KeyError:
            print('Enter user name.')
        except ValueError:
            print('Incorrect arguments number!')
        except IndexError:
            print('You entered not correct number of args')
        except TypeError:
            print('Use commands')
    return inner
    
@input_error
def add_contact(name_and_phone):   
    name, phone = name_and_phone.split(' ')
    record = phone_book.data.get(name)
    print(phone_book.data.get(name))
    if record is None:
        n = Name(name)
        p = Phone(phone)
        record = Record(n, p)
        phone_book.add_record(record)
        print(f'A new contact name: {name} phone: {phone}, has been added.')
    else:
        record.add_phone(phone)
        print('else add_phone')
    
@input_error     
def change_contact(name_and_phone):  
    name, phone, new_phone = name_and_phone.split(' ')  
    record = phone_book.data.get(name) 
    print(record)
    if name not in phone_book.keys():  
        record.add_contact(name_and_phone)  
        print(f'{name} added to contacts!')     
    else:          
        for key in phone_book.keys():            
            if key == name:
                record.change_phone(phone, new_phone)
                print(f'{key} changed his number!')             
@input_error
def del_phone(name_and_phone):
    name, phone = name_and_phone.split(' ')
    record = phone_book.data.get(name)
    for key in phone_book.keys():            
            if key == name:
                record.delete_phone(phone)
                print(f'Phone {phone} was deleted from {key} contact!')


@input_error    # Handler-для change... (дoдaвaнnя aбo oпdate)    
def phone_number(name): 
    if name in phone_book.keys():
        print(f'The phone number of {name} is {phone_book[name].phones}')
    else:
        print(f'User name {name} is not in phonebook')

@input_error
def main():
    commands = ['add', 'change', 'phones', 'hello', 'show all', 'good bye', 'close', 'exit', 'delete']
    while True:
        b = input('Enter command:')
        c = ['good bye', 'close', 'exit']
        d = b.split(' ', maxsplit = 1)[0].lower()           # command name
        if b in c:
            print('See you soon!')
            break
        elif b == 'show all':
            print(phone_book)
        elif b == 'hello':
            print('How can i help you?')
        elif b == 'help':
            print(commands)
        elif b in commands:
            print('Enter arguments to command')
        elif d == 'add':
            add_contact(b.split(' ', maxsplit = 1)[1])
        elif d == 'change':
            change_contact(b.split(' ', maxsplit = 1)[1])
        elif d == 'phones':
            phone_book.show_phones(b.split(' ', maxsplit = 1)[1])
        elif d == 'del':
            del_phone(b.split(' ', maxsplit = 1)[1])
        else:
            print('Please enter correct command. Use command "help" to see more.')
    print(phone_book)

if __name__ == "__main__":
    phone_book = AddressBook()
    main()
