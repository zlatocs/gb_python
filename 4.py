userwords = input("Введите свои слова через пробел: ")
words = []
words.append(userwords)
for i, el in enumerate(userwords.split(" "), 1):
    print(i, el[:10])