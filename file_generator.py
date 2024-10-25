from random import randint, choice

from names_lists import names, surnames

with open('input.txt', 'w', encoding='utf-8') as file:
    for i in range(randint(7, 15)):
        file.write(f'{choice(names)} {choice(surnames)} {randint(1,5)} {randint(90, 95)}\n')
