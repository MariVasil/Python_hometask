class Cells:

    def __init__(self, cores: int):
        self.cores = cores

    def __add__(self, other):
        return Cells(self.cores + other.cores)

    def __sub__(self, other):
        if (self.cores - other.cores) > 0:
            return Cells(self.cores - other.cores)
        else:
            return "разница ячеек меньше либо равна нулю"

    def __mul__(self, other):
        return Cells(self.cores * other.cores)

    def __truediv__(self, other):
        return Cells(int(self.cores / other.cores))

    def __str__(self):
        return f'клетка содержит {self.cores} ячеек'

    def make_order(self, cores_in_row: int):
        num_full_rows, num_in_last_row = divmod(self.cores, cores_in_row)
        row = '*' * cores_in_row
        result_string = (row + '\n') * num_full_rows + '*' * num_in_last_row
        return result_string


cell1 = Cells(25)
cell2 = Cells(5)

print(f'Результат сложения: {cell1 + cell2}')
print(f'Результат вычитания {cell1 - cell2}')
print(f'Результат вычитания: {cell2 - cell1}')
print(f'Результат произведения клеток: {cell1 * cell2}')
print(f'Результат деления клеток: {cell1 / cell2}')

cell3 = Cells(27)
print(cell3.make_order(5))