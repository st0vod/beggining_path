from random import sample


def is_digit():
    while True:
        n = input()
        if n.isdigit():
            return abs(int(n))
        else:
            print('Введите число')

def yes_or_no():
    while True:
        print('Напишите y - "да" или n - "нет"')
        n = input().lower()
        if n == 'y':
            return True
        elif n == 'n':
            return False
        else:
            continue

def generate_symbols():
    chars = ''
    exept = 'il1Lo0O'
    if need_digit:
        chars += digits
    if need_big_letter:
        chars += uppercase_letters
    if need_small_letter:
        chars += lowercase_letters
    if need_symbol:
        chars += punctuation
    if exept_symbol:
        exept = 'il1Lo0O?'
        for exept in chars:
            chars.replace(exept, '')
    return chars

def generate_password(number, length, chars): 
    for _ in range(number):
        print(*sample(chars, length), sep='')


digits = '0123456789'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
punctuation = '!#$%&*+-=?@^_'
chars = ''


print('_' * 50, 'Генерация пароля', sep='\n')
print('_' * 50, 'Сколько нужно сделать паролей?', sep='\n')
pas_number = is_digit()
print('_' * 50, 'Какой длины должен быть пароль?', sep='\n')
pas_length = is_digit()
print('_' * 50, 'Включить в пароль цифры?', sep='\n')
need_digit = yes_or_no()
print('_' * 50, 'Включить в пароль прописные английские буквы?', sep='\n')
need_big_letter = yes_or_no()
print('_' * 50, 'Включить в пароль строчные английские буквы?', sep='\n')
need_small_letter = yes_or_no()
print('_' * 50, 'Включить в пароль символы?', sep='\n')
need_symbol = yes_or_no()
print('_' * 50, 'Исключить неоднозначные символы il1Lo0O?', sep='\n')
exept_symbol = yes_or_no()

chars = generate_symbols()

generate_password(pas_number, pas_length, chars)

