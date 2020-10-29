from functools import reduce

digits_list = []
for digit in (el for el in range(100, 1001) if el % 2 == 0):
    digits_list.append(digit)

def my_func(el_1, el_2):
    return el_1 * el_2

print(reduce(my_func, digits_list))
