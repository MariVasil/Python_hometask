from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

i = 0
for elem in cycle(["A", "S", "A", "P"]):
    if i > 7:
        break
    print(elem)
    i += 1
