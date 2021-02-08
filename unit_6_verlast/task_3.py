class Worker:

    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class Position(Worker):
    def _init_(self, name, surname, _income):
        super().__init__(self, name, surname, _income)

    def get_full_name(self, name, surname):
        return (name, surname)

    def get_total_income(self, _income):
        return _income.get("wage") + _income.get("bonus")


example_worker = Position("Ivan", "Ivanov", "manager", 5)
print(example_worker.name)
print(example_worker.surname)
print(example_worker.position)
print(example_worker._income)
print(example_worker.get_full_name(example_worker.name, "Petrov"))
print(example_worker.get_total_income({"wage": 123, "bonus": 3}))
