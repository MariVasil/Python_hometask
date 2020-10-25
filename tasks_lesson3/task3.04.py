number1 = float(input("Введите действительное положительное число: "))
number2 = int(input("Введите целое отрицательное число: "))

if number1 < 0 or number2 >= 0:
    print("Вы ввели неправильный формат одного или обоих чисел!")
else:
    # Вариант 1
    def my_func(var_1, var_2):
        var_1 **= var_2
        return var_1


    print(f"Вариант 1: {my_func(number1, number2)}")

    # Вариант 2
    def my_func2(var_1, var_2):
        result = var_1
        for i in range(abs(var_2) + 1):
            result /= var_1
        return result


    print(f"Вариант 2: {my_func2(number1, number2)}")
