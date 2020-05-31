list = []
while True:
    user = input("Вводите: ")
    if user == '':
        print(list)
        exit()
    else:
        newline = user + '\n'
        list.append(newline)

    with open("simpletextfile.txt", "w", encoding = 'utf-8') as one:
        one.writelines(list)
