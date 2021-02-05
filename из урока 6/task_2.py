class Road:
    _length = 20
    _width = 5000

    def cover_road(self, mass, thickness):
        self.mass = mass
        self.thickness = thickness

        return self._length * self._width * self.mass * self.thickness


example_road = Road()

print(example_road.cover_road(25, 0.05))