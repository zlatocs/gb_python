seasons = ['Зима', 'Весна', 'Лето', 'Осень']
seasonsD = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
month = int(input("Введите месяц по номеру "))
if month ==1 or month == 12 or month == 2:
        print(seasonsD.get(1))
        print(seasons[0])
elif month == 3 or month == 4 or month ==5:
    print(seasonsD.get(2))
    print(seasons[1])
elif month == 6 or month == 7 or month == 8:
    print(seasonsD.get(3))
    print(seasons[2])

elif month == 9 or month == 10 or month == 11:
    print(seasonsD.get(4))
    print(seasons[3])
else:
        print("Такого месяца не существует")


