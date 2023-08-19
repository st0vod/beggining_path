def result(check):
    total = ''
    for i in check:                                               #Шифруем текст
        for j in i:
            place = letters.find(j)
            new_place = place + (len(i))
            if j in letters:
                total += letters[new_place]
            else:
                total += j
    
    new_total = ''
    for i in range(len(total)):                                    #Возвращаем исходный регистр
        if text[i].islower():
            new_total +=  total[i].lower()
        else:
            new_total += total[i]    
    return new_total    

def checking_text(text):
    text_list = []
    text = text.upper()
    temp = ''
    flag = True
    for i in range(len(text)):
        if text[i].isalpha():
            temp += text[i]
            if i == len(text) - 1:
                text_list.append(temp)                           #Для того чтобы добавить последнее слово
        elif not text[i].isalpha() and text[i-1].isalpha():      #Для того чтобы в список не добавлялись пустые ячейки
            text_list.append(temp)            
            text_list.append(text[i])
            temp = ''

        else:
            text_list.append(text[i])
    return text_list


letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'    
text = input()
check = checking_text(text)                                         #Функция на создание списка в котором слова и символы будут разделены
new_text = result(check)                                            #Функция зашифровки текса и выравнивания регистра текста
print(new_text)