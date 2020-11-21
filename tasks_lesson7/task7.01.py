class Matrix:
    def __init__(self, numbers_list: list):
        self.numbers = numbers_list

    def __str__(self):
        s = ""
        for lst in self.numbers:
            s += "\t".join(str(el) for el in lst) + "\n"
        return  s

    def __add__(self, other):
        summ_lst = []
        for i in range(len(other.numbers)):
            add_lst = []
            for j in range(len(other.numbers[i])):
                add_lst.append(self.numbers[i][j] + other.numbers[i][j])
            summ_lst.append(add_lst)
        return Matrix(summ_lst)



matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[3, 3, 3], [4, 4, 4], [5, 5, 5]])
print(matrix1)
print(matrix2)
print(matrix1 + matrix2)
