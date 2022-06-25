answer = int(input('Год рождения А.С.Пушкина ?:'))
while answer != 1799:
    print('Неверно,попробуй снова')
    answer = int(input('Год рождения А.С.Пушкина ?:'))
if answer == 1799:
    answer_1 = int(input('День рождения А.С.Пушкина ?:'))
while answer_1 != 26:
    print('Неверно,попробуй снова')
    answer_1 = int(input('День рождения А.С.Пушкина ?:'))
print('Верно')