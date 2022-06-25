answer = int(input('Год рождения А.С.Пушкина ?:'))
if answer == 1799:
    answer_1 = int(input('День рожнения А.С.Пушкина ?:'))
    if answer_1 == 26:
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверно')
print('End')

