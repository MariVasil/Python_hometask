number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))


def my_func(var_1, var_2):
    if var_2 == 0:
        return "На ноль делить нельзя!"
    else:
        return round((var_1 / var_2), 2)

print(my_func(number1, number2))

# Вариант №2
# def my_func(var_1, var_2):
#     try:
#         var_1 / var_2
#     except ZeroDivisionError:
#         return
#     return round((var_1 / var_2), 2)
#
# division = my_func(number1, number2)
#
# if division == None:
#     print("На ноль делить нельзя!")
# else:
#     print(division)
