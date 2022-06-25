while True:
    total = 5
    """
              total - количество вопросо в тесте ;
              '1840'- г.р. П.И.Чайковского
              '1834'- г.р. Д.И.Менделеева
              '1828'- г.р. Л.Н.Толстого
              '1821'- г.р. Ф.М.Достоевского
              '1810'- г.р. Н.И.Пирогова
    """
    answer = ''
    while not answer.isdigit():
        answer = (input('Год рождения П.И.Чайковского ?:'))
    answer_1 = ''
    while not answer_1.isdigit():
        answer_1 = (input('Год рождения Д.И.Менделеева ?:'))
    answer_2 = ''
    while not answer_2.isdigit():
        answer_2 = (input('Год рождения Л.Н.Толстого ?:'))
    answer_3 = ''
    while not answer_3.isdigit():
        answer_3 = (input('Год рождения Ф.М.Достоевского ?:'))
    answer_4 = ''
    while not answer_4.isdigit():
        answer_4 = (input('Год рождения Н.И.Пирогова ?:'))
    results = [answer == '1840', answer_1 == '1834', answer_2 == '1828', answer_3 == '1821', answer_4 == '1810']
    print('Количество неправильных ответов :', total - sum(results))
    print('Количество правильных ответов :', sum(results))
    print('Процент неправильных ответов :', (total - sum(results))*100/total)
    print('Процент правильных ответов :', sum(results)*100/total)
    answer_5 = ''
    while not answer_5.isalpha():
        answer_5 = (input('Хочешь пройти тест снова (ДА/НЕТ) ?:'))
    if answer_5 != 'ДА':
        break
print('До встречи !!!')
