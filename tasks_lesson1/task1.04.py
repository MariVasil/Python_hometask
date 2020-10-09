number = input("Введите целое положительное число: ")
i = 0
a = 0

while i != len(number):
    b = int(number[i])
    if a <= b:
        a = b
    i += 1
print(f"Самая большая цифра в данном числе: {a} ")
