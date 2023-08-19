
def transform_from16system(num):     #Перевод числа в 16-ю систему       
    n = [c for c in num]    #Ввод числа для перевода       
    n = n[::-1]
    total = 0
    for i in range(len(n)):
        if n[i] in system_16_letters:
            temp_index = system_16_letters.index(n[i])
            n[i] = system_16_digits[temp_index]
        total += int(n[i]) * 16 ** i
    print(total, 'В 16 системе исчисления.')

def transform_toXsystem():      #Перевод числа в заданную систему
    print('-= Для перевода числа в систему исчисления введите число. =-') 
    digit = input()             #Ввод числа для перевода
    if not digit.isdigit():
        transform_from16system(digit)
        return True
    digit = int(digit)
    print('-= В какую систему исчесления перевести данное число? =-')
    new_step = int(input())     #Основание системы с которой надо перевести
    new_digit_system = ''
    while digit > 0:
        if new_step == 16 and digit % new_step >= 10:
            temp_index = system_16_digits.index((digit % new_step))
            new_digit_system += system_16_letters[temp_index]
            digit  //= new_step
        else:
            new_digit_system += str(digit % new_step)
            digit  //= new_step    
    print(new_digit_system[::-1], f'В {new_step} системе исчисления.')
 
def transofrm_toBOH():
    print('Введите число чтобы перевести в двоичную, восмеричную и шестнадцетеричную систему.')
    n = int(input())
    bin_n = bin(n)      #Перевод числа в двоичную систему
    oct_n = oct(n)      #Перевод числа в восмеричную систему
    hex_n = hex(n)      #Перевод числа в шестнадцетеричную систему
    print(bin_n[2:], oct_n[2:], hex_n[2:].upper(), sep='\n')    
 
 
 
system_16_letters = ['A', 'B', 'C', 'D', 'E', 'F']
system_16_digits = [10, 11, 12, 13, 14, 15]      
transform_toXsystem()
#transform_toBOH()
