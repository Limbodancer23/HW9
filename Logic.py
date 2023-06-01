import con_actions

def MyLogic():
    print('1) Action with contacts. \n2) Show my phonebook\n3) Exit')
    while(True):
        n = int(input())
        if n > 3 or n < 1:
            print('- Try again please...')
        else:
            print('------------------------------')
            break

    if n == 1:
        con_actions.contact_Action()
    elif n == 2:
        show_me()
    else:
        print('Have a nice day!')

def show_me():
    n = 1
    path = 'file.txt'
    data = open(f'{path}', 'r')
    for line in data:
        print(f'{n}) {line}')
        n+=1
    data.close
    print('------------------------------')
    MyLogic()
