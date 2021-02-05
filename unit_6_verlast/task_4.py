class Car:

    def __init__(self, speed, color, name, is_police) -> object:
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return "машина поехала"

    def stop(self):
        return "Машина остановилась"

    def turn(self, direction):
        self.direction = direction
        if direction == "right":
            return "Машина повернула направо"
        else:
            return "Машина повернула налево"

    def show_speed(self, current_speed):
        self.current_speed = current_speed
        return current_speed


class TownCar(Car):
    def __init_(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, current_speed):
        self.current_speed = current_speed
        if current_speed > 60:
            return "Превышение"
        else:
            return current_speed


class WorkCar(Car):
    def __init_(self, speed, color, name, is_police):
        Car().__init__(speed, color, name, is_police)

    def show_speed(self, current_speed):
        self.current_speed = current_speed
        if current_speed > 40:
            return "Превышение"
        else:
            return current_speed

class SportCar(Car):
    def __init_(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init_(self, speed, color, name, is_police):
        Car().__init__(speed, color, name, is_police)


example_car = Car(50, "red","Mazda",  False)
print(f"Экземляр машины класса Car - эта {example_car.go()}:"
      f"\nскорость - {example_car.speed}\nцвет - {example_car.color}\n"
      f"название - {example_car.name}\nмашина полицейская - {example_car.is_police}\n"
      f"текущая скорость - {example_car.show_speed(49)}")

print(example_car.turn("left"))
print(example_car.stop())



example_carTownCar = TownCar(50,"green", "Juke",False)
print(f"\nЭкземляр машины класса TownCar - эта {example_carTownCar.go()}:"
      f"\nскорость - {example_carTownCar.speed}\nцвет - {example_carTownCar.color}\n"
      f"название - {example_carTownCar.name}\nмашина полицейская - {example_carTownCar.is_police}\n"
      f"текущая скорость - {example_carTownCar.show_speed(40)}")

print(example_carTownCar.turn("left"))
print(example_carTownCar.stop())

example_carWorkCar = WorkCar(50, "баклажан","ВАЗ", False)
print(f"\nЭкземляр машины класса WorkCar - эта {example_carWorkCar.go()}:"
      f"\nскорость - {example_carWorkCar.speed}\nцвет - {example_carWorkCar.color}\n"
      f"название - {example_carWorkCar.name}\nмашина полицейская - {example_carWorkCar.is_police}\n"
      f"текущая скорость - {example_carWorkCar.show_speed(61)}")
print(example_carWorkCar.turn("right"))
print(example_carWorkCar.stop())

example_carWorkCar = WorkCar(50, "баклажан","ВАЗ", False)
print(f"\nЭкземляр машины класса WorkCar - эта {example_carWorkCar.go()}:"
      f"\nскорость - {example_carWorkCar.speed}\nцвет - {example_carWorkCar.color}\n"
      f"название - {example_carWorkCar.name}\nмашина полицейская - {example_carWorkCar.is_police}\n"
      f"текущая скорость - {example_carWorkCar.show_speed(61)}")
print(example_carWorkCar.turn("right"))
print(example_carWorkCar.stop())
example_carSportCar= SportCar(90, "white","Kia", False)
print(f"\nЭкземляр машины класса SportCar - эта {example_carSportCar.go()}:"
      f"\nскорость - {example_carSportCar.speed}\nцвет - {example_carSportCar.color}\n"
      f"название - {example_carSportCar.name}\nмашина полицейская - {example_carSportCar.is_police}\n"
      f"текущая скорость - {example_carSportCar.show_speed(101)}")
print(example_carSportCar.turn("right"))
print(example_carSportCar.stop())

example_carPoliceCar= PoliceCar(43, "болотный","УАЗ", True)

print(f"\nЭкземляр машины класса PoliceCar - эта {example_carPoliceCar.go()}:"
      f"\nскорость - {example_carPoliceCar.speed}\nцвет - {example_carPoliceCar.color}\n"
      f"название - {example_carPoliceCar.name}\nмашина полицейская - {example_carPoliceCar.is_police}\n"
      f"текущая скорость - {example_carPoliceCar.show_speed(61)}")
print(example_carPoliceCar.turn("right"))
print(example_carPoliceCar.stop())
