class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  #matrix=list[list[int]]

        for el in range(len(self.list_1)):

            for el_2 in range(len(self.list_2[el])):
                matrix[el][el_2] = self.list_1[el][el_2] + self.list_2[el][el_2]

        return str('\n'.join(['\t'.join([str(el_2) for el_2 in el]) for el in matrix]))


my_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(my_matrix.__add__())
"""
list_1=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_2=[[9, 8, 7], [6, 5, 4], [3, 2, 1]]
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for el in range(len(list_1)):

    for el_2 in range(len(list_2[el])):

        print(list_1[el][el_2])
        print(list_2[el][el_2])
        matrix[el][el_2] = list_1[el][el_2] + list_2[el][el_2]
print(matrix)
"""