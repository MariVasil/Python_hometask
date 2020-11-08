# -*- coding: utf-8 -*-

change_dict = {'One': 'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}

with open("file_task5.4.txt") as my_file:
    with open("new_file.txt", "w") as my_new_file:
        for item in my_file:
            parts = item.split(" — ")
            my_new_file.write(f"{change_dict[parts[0]]} — {parts[1]}")