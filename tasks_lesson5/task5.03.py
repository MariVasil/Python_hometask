with open("salaries_task5.3.txt") as my_file:
    salary_list = []
    for item in my_file:
        parts = item.split(" ")
        salary_list.append((parts[0], float(parts[1].replace("\n", ""))))

    average_salary = 0.0
    under_20_list = []
    for elem in salary_list:
        if elem[1] < 20000:
            under_20_list.append(elem[0])
        average_salary += elem[1]
    average_salary /= len(salary_list)
    print(f"Средняя величина дохода сотрудников: {round(average_salary, 2)}")
    if len(under_20_list) == 0:
        print("Нет сотрудников с доходом ниже 20 000.00")
    else:
        print(f"Сотрудники с доходом ниже 20 000.00: ")
        for el in under_20_list:
            print(el)
