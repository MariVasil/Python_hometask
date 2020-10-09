revenue = int(input("Выручка компании, руб: "))
cost = int(input("Издержки компании, руб: "))
result = revenue - cost

if revenue == cost:
    print("Выручка и издержки равны")
elif revenue > cost:
    print(f"Прибыль компании: {result} руб.")
    print(f"Рентабельность: {round((result / revenue * 100), 2)} %")
    staff = int(input("Количество сотрудников в компании: "))
    print(f"Прибыль в расчёте на одного сотрудника: {round((result / staff), 2)} руб")
else:
    print(f"Убыток компании: {-result} руб.")
