class Cell:
    def __init__(self, amount) -> object:
        self.amount = int(amount)


    def __add__(self, other):
        return Cell(self.amount + other.amount)

    def __sub__(self, other):
        if self.amount - other.amount <= 0:
            return "Деление невозможно"
        else:
            return Cell(self.amount - other.amount)

    def __mul__(self, other):
        return Cell(self.amount * other.amount)

    def __truediv__(self, other):
        return Cell(int(self.amount / other.amount))

    def __str__(self):
        return f'Итог {self.amount}'

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(cells_in_row/self.amount)):
            row += f'{"*" * self.amount}\\n'
        row += f'{"*" * ( cells_in_row %  self.amount)}'
        return row

cells1 = Cell(5)
cells2 = Cell(5)
print(cells1 + cells2)
print(cells1 - cells2)
print(cells2 * cells1)
print(cells1 / cells2)
print(cells1.make_order(12))
print(cells2.make_order(15))