digit_list = [1, 45, 5, 67, 123, 9, 15, 1589, 45, 767]


def digit_sorting(list):
    for i in range(1, len(list)):
        if list[i] > list[i - 1]:
            yield list[i]


final_list = []
for digit in digit_sorting(digit_list):
    final_list.append(digit)
print(final_list)
