from random import randint

def choice(name, list_answer):
    while True:
        question = input()
        print('_' * 50)
        print(f'Ты хочешь узнать "{question}"')
        a_length = len(list_answer)
        print('Мой ответ:', list_answer[randint(0, a_length)])
        if is_valid(name):
            break
              
def is_valid(name):
    print(f'{name} хочешь задать еще вопрос? Напиши да или нет.')
    while True:
        yes_no = input().lower()
        if yes_no == 'да':
            print(f'Хорошо {name}, тогда какой твой следующий вопрос?')
            return False
        elif yes_no == 'нет':
            print(f'Тогда закончим предсказания! Пока {name}!')
            return True
        else:
            print('Напиши да или нет!')

ball_list_answers = [
    'Бесспорно', 'Мне кажется - да', 'Пока неясно, попробуй снова', 'Даже не думай', 'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет',
    'Никаких сомнений', 'Хорошие перспективы', 'Лучше не рассказывать', 'По моим данным - нет', 'Определённо да', 'Знаки говорят - да',
    'Сейчас нельзя предсказать', 'Перспективы не очень хорошие', 'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно'
    ]
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Как тебя зовут? ')
print('Привет', name)
print('_' * 50)
print('Какой вопрос ты хочешь мне задать?')
choice(name, ball_list_answers)