number = int(input("Введите целое число: "))
number2 = number
sum = number

for i in range(2):
    number2 = int(str(number2) + str(number))
    sum += number2

print(f"Итоговая сумма: {sum}")
