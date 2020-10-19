my_list = [7, 5, 3, 3, 2]

user_rate = int(input("Новый элемент рейтинга: "))
for i in range(len(my_list)+1):
    if i == len(my_list) or user_rate > my_list[i]:
        my_list.insert(i, user_rate)
        break
print(my_list)