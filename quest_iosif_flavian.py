print('Задача Иосифа Флавия')
print('"x" человек стоят в кругу, они пронумерованы от x до 1 и начинают считаться, каждый "n" человек выбывает')
print('Введите количество человек.')
n = int(input())
print('Введите шаг выбывания')
k = int(input())
list_person = [i for i in range(1, n + 1)]
while len(list_person) > 1:
    for j in range(0, k - 1):
        list_person.append(list_person[j])
    del list_person[:k]
print('Угадайте какой номер останется последним!')
answer = int(input())
if answer == list_person[0]:
    print('Угадали!')
else:
    print('Не угадали! Правильный ответ:', list_person[0])
