while True:
    i = input("Введите строку для добавления в файл. Для прекращения ввода просто нажмите Enter: ")
    if i == "":
        break
    else:
        my_file = open("new_file.txt", 'a')
        my_file.write(i + "\n")
        my_file.close()