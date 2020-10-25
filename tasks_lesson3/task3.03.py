number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
number3 = int(input("Введите третье число: "))


def my_func(var_1, var_2, var_3):
    numbers_list = [var_1, var_2, var_3]
    numbers_list.sort
    return numbers_list[1] + numbers_list[2]
    # Вариант 2
    # a = max(numbers_list)
    # numbers_list.remove(a)
    # b = max(numbers_list)
    # return a + b


print(my_func(number1, number2, number3))
