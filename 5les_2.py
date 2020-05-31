with open("5less.2.txt", "r", encoding="utf-8") as file:
    file_len = file.readlines()
    print(f"Строк: {len(file_len)}")
    count = 0
    for i in file_len:
        count += 1
        print(f"Слов в {count} строке: {len(i.split())}")
