from random import *
print('Угадайте число')
random_integer = randint(1, 100)
while True:   
    num = int(input())
    if num == random_integer:
        print('Вы угадали, поздравляем!')
        break
    elif num < random_integer:
        print('Слишком мало, попробуйте еще раз')        
    else:
        print('Слишком много, попробуйте еще раз')
print('Правильно, загаданное число :', random_integer)



