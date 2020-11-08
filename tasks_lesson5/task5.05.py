# -*- coding: utf-8 -*-

import random

with open("file_task5.5.txt", "w") as my_file:
    for i in range(10):
        my_file.write(f"{random.randint(0, 1000)}")
        if i != 9:
            my_file.write(" ")

with open("file_task5.5.txt") as my_file_2:
    content = my_file_2.readline().split(" ")
    sum = 0
    for elem in content:
        sum += int(elem)
    print(f"Сумма чисел в файле: {sum}")
