# Реализовала с использованием функции, поскольку урок был про функции. Но в текущей задаче было бы проще реализовать просто циклом.

def my_func(var_1):
    numbers_sum = 0
    global need_exit
    for i in var_1:
        if i == "&":
            need_exit = True
            break
        numbers_sum += float(i)
    return numbers_sum


final_sum = 0
need_exit = False
while not need_exit:
    input_numbers = input("Для суммирования добавьте числа через пробел. Для выхода введите &: ")
    numbers_list = input_numbers.split()
    final_sum += my_func(numbers_list)

    print(f"Итоговая сумма: {final_sum}")
