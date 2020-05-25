list1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print(f'Исходный список: {list1}')

def max_ascendent_values_in_list(input_list: list):
    output_list = []
    for key, value in enumerate(input_list):
        if key+1 < len(input_list) and value < input_list[key+1]:
            output_list.append(input_list[key+1])

    return output_list

print(f'Результат: {max_ascendent_values_in_list(list1)}')