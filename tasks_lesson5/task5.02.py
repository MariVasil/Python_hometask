# -*- coding: utf-8 -*-

my_file = open("file_task5.2.txt", "r")
content = my_file.readlines()
print(f"Количество строк в файле {my_file.name} - {len(content)}")
my_file.close()

for ind, line in enumerate(content, 1):
    line = line.replace("\n", "")
    print(f"Количество знаков в {ind}-й строке - {len(line)}")