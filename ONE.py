def my(a, b):
    print(a // b)
try:
    my(int(input('Введите число:')), int(input('Введите второе число:')))
except ZeroDivisionError:
    print('Нельзя поделить на ноль.')











