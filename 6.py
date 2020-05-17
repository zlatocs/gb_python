userAnswer = input("Добавить товары (да/нет)?: ")
goods = []
list = ["название", "цена", "количество", "ед"]
i = 1
n = 0
statistics = {}

while userAnswer.lower() == "да":
    userDict = {}
    for el in list:
        userDict[el] = input(f"Введите {el}: ")
    goods.append((i, userDict))
    userAnswer = input("Добавить еще товар (да/нет)? ")
    i += 1
else:
    print(goods)
    for it in list:
        n = 0
        tmp_list = []
        for el in goods:
            tmp_dict = goods[n][1]
            tmp_list.append(tmp_dict.get(it))
            n += 1
            statistics.update({it: tmp_list})
        n += 1
for goods in goods:
    print(goods)
print("Goodbye!")