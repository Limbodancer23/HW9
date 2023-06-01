import Logic
def contact_Action():
    print(' Select action\n1) Add new contact.\n2) Change contact\n3) Delete contact\n4) Search contact with keyword\n5) Back')
    while(True):
        n = int(input())
        if n > 5 or n < 1:
            print('- Try again please...')
        else:
            print('------------------------------')
            break
    if n == 1:
        add_Contact()
    elif n == 2:
        change_Contact()
    elif n == 3:
        delete_con()
    elif n == 4:
        search_con()
    elif n == 5:
        Logic.MyLogic()

def add_Contact():
    name = input('Please input name of contact: ')
    S_same = input('Please input second name of contact: ')
    num = input('Please input phone number of contact: ')
    print('------------------------------')
    contact = [name, S_same, num]
    data = open('file.txt', 'a')
    data.writelines(f'{contact}\n')
    data.close()
    contact_Action()

def change_Contact():
    with open('file.txt', 'r') as data:
        lines = data.readlines()
        target_contact = int(input('Select contact: '))
        name = input('Please input name of contact: ')
        S_same = input('Please input second name of contact: ')
        num = input('Please input phone number of contact: ')
        contact = [name, S_same, num]
        lines.pop(target_contact-1)
        lines.insert(target_contact-1,f'{contact}\n')
    with open('file.txt', 'w') as data:
        data.writelines(lines)
    print('------------------------------')
    contact_Action()


def delete_con():
    with open('file.txt', 'r') as data:
        lines = data.readlines()
    target_contact = int(input('Select contact: '))
    lines.pop(target_contact-1)
    with open('file.txt', 'w') as data:
        data.writelines(lines)
    print('------------------------------')
    contact_Action()

def search_con():
    n=1
    key_Word = input('Enter keyword for seeking contact:\n')
    path = 'file.txt'
    data = open(f'{path}', 'r')
    for line in data:
        if key_Word in line:
            print(f'{n}) {line}')
    print('------------------------------')
    contact_Action()