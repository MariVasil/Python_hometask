class IsNotDigit(Exception):
    pass


final_list = []

while True:
    try:
        input_string = input(f'Для окончания введите stop.\nВведите новый элемент: ')
        if input_string == 'stop':
            print(f'Вы остановили заполнение списка. Список: {final_list}')
            break
        elif input_string.isdigit():
            final_list.append(input_string)
        else:
            raise IsNotDigit('Ошибка. Необходимо ввести число.')
    except IsNotDigit:
        print('Ошибка. Необходимо ввести число.')
