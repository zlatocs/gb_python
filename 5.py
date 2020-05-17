my_list = [7,4,3,3,2]
a = int(input("Добавьте цифру в рейтинг: "))
my_list.append(a)
my_list = sorted(my_list)
my_list1 = my_list[::-1]
print(my_list1)