import sys

try:
    file, working_hours, rate, bonus = sys.argv
except ValueError:
    print("Invalid arguments")
    exit()


def salary(var_1, var_2, var_3):
    return var_1 * var_2 + var_3

print(f"Ваша заработная плата составит: {salary(int(working_hours), int(rate), int(bonus))}")
