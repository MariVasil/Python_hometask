digit_list = [1, 1, 1, 45, 5, 5, 67, 123, 123, 9, 15, 1589, 1, 45, 767, 5]


def digit_filter(list_in):
    for i in list_in:
        if list_in.count(i) == 1:
            yield i

final_list = []
for digit in digit_filter(digit_list):
    final_list.append(digit)
print(final_list)
