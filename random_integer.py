from random import randint
from math import log2, ceil


def minimum_guess(a, b, r_integer):
    left = a
    right = b
    counter = 0
    while True:
        middle = (left + right) // 2
        counter += 1
        if middle == r_integer:
            return counter
        elif middle < r_integer:
            left = middle + 1
        else:
            right = middle - 1


def is_valid(text, a, b):
    while True:
        if text.isdigit() and a <= int(text) <= b:
            return int(text)
        elif not text.isdigit():
            print(f'Введите ТОЛЬКО цыфру в диапозоне [{a}:{b}]')
            text = input()
        else:
            print(f'Вводить цыфру надо только в диапозоне [{a}:{b}]')
            text = input()


def is_valid_ab():
    while True:
        print('Введите первое число:')
        a = input()
        print('Введите второе число:')
        b = input()
        if not a.isdigit() or not b.isdigit():
            print('Необходимо ввести только числа')
            continue
        elif int(a) > int(b):
            print('Первое число должно быть меньше второго')
            continue
        else:
            return int(a), int(b)


def is_answer(text):
    while True:
        text.lower()
        if text == 'да':
            print('Продолжим игру!')
            return False
        elif text == 'нет':
            print('Конец игры!')
            return True
        else:
            print('Ввести надо либо "да" либо "нет"')
            text = input()


def game_body():
    print('Необходимо ввести два числа в диапазоне которых будет находиться загаданное число')
    a, b = is_valid_ab()
    print(f'Загаданное число находиться в диапазоне [{a}:{b}]')
    random_integer = randint(a, b)
    print('А теперь угадайте число')
    counter = 0
    while True:
        num = is_valid(input(), a, b)
        counter += 1
        if num == random_integer:
            print('Вы угадали, поздравляем!')
            break
        elif num < random_integer:
            print('Слишком мало, попробуйте еще раз')
        else:
            print('Слишком много, попробуйте еще раз')
    print('Загаданное число :', random_integer)
    print(f'Вы отгадали число {random_integer} с {counter} попытки')
    print(
        f'Наименьее число догадок,  чтобы отгадать число в диапазоне [{a}:{b}] использвуя двоичный логорифм - ', ceil(log2(b)))


# start programm
print('-' * 43, '***Добро пожаловать в числовую угадайка ***', '-' * 43, sep='\n')
while True:
    game_body()
    print('Ещё заход?', 'Напишите "да", чтобы продолжить угадывать или "нет", чтобы прекратить игру', sep='\n')
    if is_answer(input()):
        break


