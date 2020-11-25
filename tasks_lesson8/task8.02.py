class ZeroDivision(Exception):
    pass


try:
    a = float(input('Введите делимое: '))
    b = float(input('Введите делитель: '))
    if b == 0:
        raise ZeroDivision()
    else:
        print(a / b)
except ZeroDivision:
    print('Делить на ноль нельзя')