rev = int(input('Введите вашу выручку: '))
cost = int(input('Введите ваши издержки: '))
staff = int(input('Введите кол-во сотрудников: '))

if rev > cost:
    print("Фирма работает в плюс!")
    profit = rev - cost
    print("Прибыль составляет: %d"%(profit))
    rent = profit // rev
    print("Рентабельность составляет: %d процентов "%(rent))
    profitForStaff = profit / staff
    print('Прибыль фирмы в расчете на одного сотрудника составляет: %d'%(profitForStaff))
    # не могу понять, как высчитать рентабельность, so bad math. Но мы же про программирование, а не математику? ;)

else:
    print('Фирма работает в минус, пора ее закрыть :c ')


