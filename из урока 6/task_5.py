class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return "Запуск отрисовки"



class Pen(Stationery):


    def draw(self):
        return "Запуск карандашной отрисовки"


class Pencil(Stationery):

    def draw(self):

        return 'Запуск  отрисовки ручкой'


class Handle(Stationery):
   def draw(self):
       return "Запуск  отрисовки маркером"


exampleStationery = Stationery("Рисуй")

print(exampleStationery.draw())
exampleStationeryPen = Pen(Stationery)

print(exampleStationeryPen.draw())
exampleStationeryPencil = Pencil(Stationery)

print(exampleStationeryPencil.draw())
exampleStationeryHandle = Handle(Stationery)

print(exampleStationeryHandle.draw())