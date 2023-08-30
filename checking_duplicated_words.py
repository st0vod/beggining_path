from colorama import init, Fore, Back, Style

def inputing_small_words():
    print(Fore.BLACK + Back.WHITE + 'Хотите добавить слова исключения, чтобы программа их не выделяла, как дублирующие? Напишите "yes" или "no"')
    answer = check_answer()
    while answer:
        print(Fore.BLACK + Back.WHITE + 'Напишите через пробел слова в нижнем регистре')
        words = input()
        print(Fore.BLACK + Back.WHITE + 'Вы ввели:')
        print(Fore.YELLOW + f'{words}')
        print(Fore.BLACK + Back.WHITE + 'Всё правильно? Напишите "yes" или "no", чтобы подтвердить добавление слов')
        answer2 = check_answer()
        if answer2:
            print(Fore.BLACK + Back.WHITE + 'Добавленые слова:')
            print(Fore.YELLOW + f'{words}')            
            words = words.upper().split()
            for word in words:
                small_words.append(word)
        else:
            continue
        print(Fore.BLACK + Back.WHITE + f'Хотите добавить ещё слова? Напишите "yes" или "no"')
        answer = check_answer()
        if not answer:
            break
def check_answer():
    text = input().lower()
    while(True):
        if text == 'no':
            return False
        elif text == 'yes':
            return True
        else:
            print(Fore.BLACK + Back.WHITE + 'Напишите "yes" или "no"')
            text = input().lower()
            
def check_word(el):
    if len(el) > 2 and el not in small_words:
        if not el[0].isalpha() and not el[-1].isalpha():
            el = el[1:-1]
        elif not el[0].isalpha and el[-1].isalpha():
            el = el[1:]
        elif el[0].isalpha and not el[-1].isalpha():
            el = el[:-1]
    return el 
def inputing_text():
    text = []
    while True:
        check_text = input()
        if check_text == 'start scan':
            print()
            print()
            return text
        text.append(check_text)            

def preparing_lists(text):
    for i in range(len(text)):
        copy_text.append(text[i].upper().split())    
        text[i] = text[i].split()
        for j in range(len(copy_text[i])):
            word = check_word(copy_text[i][j])
            if word in new_text and len(word) > 2 and word not in small_words:
                if word not in reapeted_words:
                    reapeted_words.append(word)                                    
            else:
                new_text.append(word)
                
def menu():
    print(Fore.BLACK + Back.WHITE + "ПРОГРАММА ДЛЯ ПРОВЕРКИ ПОВТОРЕНИЙ СЛОВ В ТЕКСТЕ")
    print()
    print(Fore.BLACK + Back.WHITE + "МЕНЮ:")
    print('Выберете действие:')
    print('1. Просканировать текст на наличие дублирующих слов'.ljust(30),  '- введите "1"')
    print('2. Добавить слова исключения'.ljust(30), '- введите "2"')   
    flag = True
    while flag:
        answer = input()
        if answer == '2':            
            inputing_small_words()
            print(Fore.BLACK + Back.WHITE + "ТЕПЕРЬ ПРОВЕРИМ ДУБЛИРУЮЩИЕ СЛОВА В ТЕКСТЕ")
            print(Fore.BLACK + Back.WHITE + "Введите текст для проверки, после напишите в косоли 'start scan', чтобы сканировать текст ")
            flag = False
        elif answer == '1':
            print(Fore.BLACK + Back.WHITE + "Введите текст для проверки, после напишите в косоли 'start scan', чтобы сканировать текст ")
            flag = False
        else:
            print('Введите "1" или "2"')
def body_programm():
    text = inputing_text()
    preparing_lists(text)
    text_in_one_str = ''
    print(Back.GREEN + " ", Back.RED + " ", Back.YELLOW + " ")
    for i in range(len(text)):
        for j in range(len(text[i])):
            word = check_word(copy_text[i][j])
            text_in_one_str += text[i][j].upper()
            if word in reapeted_words and word not in small_words:
                text[i][j] = Style.BRIGHT + Fore.RED + text[i][j]
        print(*text[i])    
    print(Back.GREEN + " ", Back.RED + " ", Back.YELLOW + " ")    
    return text_in_one_str

init(autoreset=True) 
small_words = ['ИЛИ', 'ДЛЯ', 'ПОД', 'НАД', 'НАС', 'КАК', 'ЕЩЕ', 'ЕЩЁ', 'УЖЕ', 'ВЫ', 'МЫ', 'БЕЗ', 'ВСЕ', 'СМ']
while True:
    reapeted_words = []
    new_text = []
    copy_text = []   
    menu()
    text_in_one_str = body_programm()
    print(Fore.BLACK + Back.WHITE + f'Всего "{len(reapeted_words)}" часто повторяющихся слов:')          
    for el in reapeted_words:
        print(Back.YELLOW + Fore.BLACK + f'{el.ljust(15)} {text_in_one_str.count(el)}')
    print(Fore.BLACK + Back.WHITE + 'Хотите вернтуться в главное меню? Введите "yes" или "no')
    flag = check_answer()
    if not flag:
        break

print(Fore.BLACK + Back.WHITE + 'Чтобы выйти, нажмите ENTER')
stop_console = input()