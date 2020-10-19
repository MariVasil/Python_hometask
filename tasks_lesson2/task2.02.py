quantity = int(input("Сколько элементов вы хотите добавить в список: "))
list = []

for i in range(quantity):
    new_value = input(f"Добавьте {i}-й элемент списка: ")
    list.append(new_value)

print(f"Ваш первоаначальный список: {list}")

for i in range(int(quantity / 2)):
    list[i*2], list[i*2+1] = list[i*2+1], list[i*2]

print(f"Ваш изменённый список: {list}")
