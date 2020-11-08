with open("file_task5.6.txt") as my_file:
    subjects_dict = {}
    for item in my_file:
        part_1 = item.split(":")
        part_2 = part_1[1].split(" ")
        sum = 0
        for part in part_2:
            ind = part.find("(")
            if ind != -1:
                sum += int(part[:ind])
        subjects_dict[part_1[0]] = sum
    print(subjects_dict)