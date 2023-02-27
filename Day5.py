'''Project = Python Password Generator'''

import random

letters = ['a' ,'b','c','d','e','f','g','h','i','j','k','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

number = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','#','$','%','&','{','}','*','+']

print("Wellcome to the Python Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like ?\n"))
nr_numbers = int(input(f"How many number would you like ?\n"))



def easy():
    password = ""
    'EASY PASSWORD'
    for char in range(1 , nr_letters+1):
        password += random.choice(letters)
        'random_char = random.choice(letters)'
        'password = password + random_char'
    for char in range(1 , nr_symbols+1):
         password += random.choice(symbols)

    for char in range(1 , nr_numbers+1):
        password += random.choice(number)

    print("\n****************Here is your Easy Password*****************\n")
    print(password)



def hard():
    '''HARD level'''

    password_list = []

    for char in range(1 , nr_letters+1):
        password_list.append(random.choice(letters))
        'random_char = random.choice(letters)'
        'password_list = password_list + random_char'
    for char in range(1 , nr_symbols+1):
        password_list += random.choice(symbols)

    for char in range(1 , nr_numbers+1):
        password_list += random.choice(number)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char


    print("\n****************Here is your Strong Password*****************\n")
    print(password)


ch = int(input("1 = Easy Password \n2 = Hard Password\n"))

def switch(ch):
    if ch == 1:  easy()
        
    elif ch == 2:  hard()

switch(ch)
