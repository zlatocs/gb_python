with open("text_3.txt", "r", encoding="utf-8") as obj:
    summ = []
    less = []
    line = obj.read().split('\n')
    for i in obj:
        i = i.split()
        if float(i[1]) < 20000:
            less.append(i[0])
        sum.append(i[1])
print(f'Зарплаты меньше 20000 {less}. Выше {sum(map(float,summ)) / len(summ)}')








