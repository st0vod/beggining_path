from random import randint

def display_hangman(tries):
     stages = [ 
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
     return stages[tries]   

def get_word():
     return word_list[randint(0, len(word_list) - 1)].upper()

def play(word):
     word_completion = '_' * len(word)
     guessed = False
     guessed_letters = []
     guessed_words = []
     tries = 6
     
     print('Давайте играть в угадайку слов!')
     print(display_hangman(tries))
     print(word_completion)
     
     while True:
          if word == word_completion:
               print(f'Поздравляю, ты угадал! Это слово {word}')
               break
          temp_answer = input().upper()
          if temp_answer.isalpha:
               if temp_answer not in guessed_letters and temp_answer not in guessed_words:                    
                    if temp_answer == word:
                         print(f'Поздравляю, ты угадал! Это слово {word}') 
                         break
                    elif temp_answer in word:                              
                         temp = ''
                         for i in range(len(word)):
                              if word[i] == temp_answer:
                                   temp += word[i]
                              else:
                                   temp += word_completion[i]
                         word_completion = temp                             
                         print(word_completion)
                         guessed_letters.append(temp_answer)
                         continue        
                    elif len(temp_answer) > 1:
                         guessed_words.append(temp_answer)
                    else:
                         guessed_letters.append(temp_answer)
               else:
                    print('Это слово или буква уже были введены, попробуй другие')
                    continue
          else:
               print('Вводи либо слово либо букву!')
               continue
          tries -= 1
          print(display_hangman(tries))
          print('Нет, не угадал! Попробуй еще.')
          print(word_completion)
          if tries == 0:
               print(f'Загаданое слово было {word}')
               break
          
def replay():
     print('Хочешь сыграть еще?')
     print('Напиши "y" - да или "n" - нет')
     while True:
          answer = input()
          if answer == 'y':
               return False
          elif answer == 'n':
               print('КОНЕЦ ИГРЫ')
               return True
          else:
               print('Напиши "y" - да или "n" - нет')
     



word_list = [
    'книга', 'компьютер', 'телефон', 'диван', 'машина', 'холодильник', 'дом',
    'гараж', 'автомат', 'солдат', 'танк', 'самолет', 'шпага', 'лошадь', 'собака', 'котенок'
]

while True:
     word = get_word()
     play(word)
     if replay():
          break