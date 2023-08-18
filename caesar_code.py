def yes_or_no():
    while True:
        print('Чтобы зашифровать напишите "y", чтобы расшифровать напишите "n"')
        answer = input()
        if answer == 'y':
            print('<<<Текст будет зашифрован>>>')
            return True
        elif answer == 'n':
            print('<<<Текст будет расшифрован>>>')
            return False
        else:
            print('Напишите "y" или "n"')


def choice_language():
    print('Выберете язык:', 'Русский - напишите "ru"', 'Английский - напишите "en"', sep='\n')
    while True:
        language = input()
        if language == 'ru':
            print('<<<Текст будет на русском языке>>>')
            return language
        elif language == 'en':
            print('<<<Текст будет на английском языке>>>')
            return language
        else:
            print('Напиши "ru" или "en"')


def upload_step(lang):
    limit_step = 0
    if lang == 'ru':
        limit_step = 33
    else:
        limit_step = 26
    print('Какой будет шаг сдвига?')
    while True:
        step = input()
        if step.isdigit() and 1 <= int(step) <= limit_step:
            return int(step)
        else:
            print(f'Напиши цифру - шаг сдвига, шаг не может превышать {limit_step}')


def processing_programm(text, crypt, lang, step):
    total = ''
    text = text.upper()
    if crypt:       #шифруем текст
        if lang == 'ru':
            for i in text:
                place = upcase_ru.find(i)  #делаем поиск символа с начала строки
                new_place = place + step
                if i in upcase_ru:
                    total += upcase_ru[new_place]
                else:
                    total += i
        else:
            for i in text:
                place = upcase_en.find(i)
                new_place = place + step
                if i in upcase_en:
                    total += upcase_en[new_place]
                else:
                    total += i            
    else:           #расшифровываем текст
        if lang == 'ru':
            for i in text:
                place = upcase_ru.rfind(i)  #делаем поиск символа с конца строки
                new_place = place - step
                if i in upcase_ru:
                    total += upcase_ru[new_place]
                else:
                    total += i
        else:
            for i in text:
                place = upcase_en.rfind(i)
                new_place = place - step
                if i in upcase_en:
                    total += upcase_en[new_place]
                else:
                    total += i           
    return total    
    
    
    
    
upcase_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
upcase_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

encrypt = yes_or_no()           #шифровать или расшифровывать
language = choice_language()    #выбор языка
step = upload_step(language)            #шаг шифровки

print('Введи текст')
text = input()
total = processing_programm(text, encrypt, language, step)
new_total = ''
for i in range(len(total)):
    if text[i].islower():
        new_total +=  total[i].lower()
    else:
        new_total += total[i]
print(new_total)