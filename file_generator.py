from random import randint, choice

from names_lists import names, surnames

with open('input.txt', 'w', encoding='utf-8') as file:
    for i in range(randint(5, 10)):
        file.write(f'{choice(names)} {choice(surnames)} {randint(9, 11)} {randint(90, 95)}\n')
