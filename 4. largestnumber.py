usernumber = int(input("Введите целое положительное число: "))

max = usernumber%10

usernumber = usernumber//10

while usernumber > 0:

   if usernumber%10 > max:

       max = usernumber%10

   usernumber = usernumber//10

print("Максимальная цифра из вашего числа: " + str(max))