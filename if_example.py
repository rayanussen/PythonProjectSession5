rom random import choice


drinks = ['whiskey', 'rum', 'tequila', 'gin', 'sake', 'wine', 'beer', 'vodka', 'HENNESSY']
mixers = ['coke', 'tonic', 'oj', 'cranberry', 'sprite', 'ginger ale', 'soda', 'lemonade', 'lime juice']


print('I am the virtual bartender, welcome to my humble bar')
name = input('What is your name? ')

try:
    age = int(input(f'How old are you {name}? '))
    legal = None
    country = input('What country are you from? ')
    if age < 14:
        legal = False
    elif age < 16:
        if country == 'Austria':
            legal = True
        else:
            legal = False
    elif age < 18:
        if country == 'Austria' or country == 'Luxembourg' or country == 'Germany':
            legal = True
        else:
            legal = False
    elif age < 21:
        if country == 'USA' or country == 'UAE':
            legal = False
        else:
            legal = True
    else:
        legal = True

    if legal:
        print(f'Here is a {choice(drinks)}-{choice(mixers)}')
    else:
        print(f'I can only serve you {choice(mixers)}')


except ValueError:
    print('I dont have time for your games, get out!')