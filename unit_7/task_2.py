
class Clothes:
    def __init__(self, Size, Growth):
        self.Size = Size
        self.Growth = Growth

    def consumption_coat(self):
        return round(self.Size / 6.5 + 0.5, 2)

    def consumption_custume(self):
        return round(self.Growth * 2 + 0.3, 2)

    @property
    def consumption(self):
        return f'Итог: {(round(self.Size / 6.5 + 0.5 + self.Growth * 2 + 0.3, 2))}'


class Coat(Clothes):
    def __init__(self, Size, Growth):
        super().__init__(Size, Growth)


class Custume(Clothes):
    def __init__(self, Size, Growth):
        super().__init__(Size, Growth)



coat = Coat(2, 6)
custume = Custume(9, 6)
print(coat.consumption_coat())
print(custume.consumption_custume())
print(coat.consumption)
print(custume.consumption)

