dict = {}
with open('text_6.txt') as obj:
    for line in obj:
        name, stats = line.split(':')
        name_sum = sum(map(int,"".join([i for i in stats if i == ' ' or (i >= '0' and i <= '9')]).split()))
        dict[name] = name_sum
print(f'{dict}')