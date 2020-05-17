arr = []
n = int(input("Введите количество элементов : ")) # не понял, как сделать список неограниченный кол-вом элементов

for i in range(0, n):
    newElement = (input())

    arr.append(newElement)


j = 0
for i in range(int(len(arr) / 2)):
    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    j += 2

print(arr)
