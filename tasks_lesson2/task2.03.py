user_month = int(input("Введите номер месяца от 1 до 12: "))

if user_month > 12 or user_month <= 0:
    print("Месяца с таким номером не существует")
else:
    # List
    seasons = ["Зима", "Весна", "Лето", "Осень"]
    print(f"{user_month}-й месяц - {seasons[int(user_month/3)]}")


    # Dictionary
    months = {1: 'Зима', 2: 'Зима', 3: 'Весна',
              4: 'Весна', 5: 'Весна', 6: 'Лето',
              7: 'Лето', 8: 'Лето', 9: 'Осень',
              10: 'Осень', 11: 'Осень', 12: 'Зима'}
    print(f"{user_month}-й месяц - {months[user_month]}")
