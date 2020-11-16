class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_total_income(self):
        print(f"Wage+bonus = {self._income['wage'] + self._income['bonus']}")


Brown = Position("Bobby", "Brown", "Manager", {"wage": 12000, "bonus": 2000})
Brown.get_full_name()
Brown.get_total_income()

Smith = Position("John", "Smith", "Agent", {"wage": 8000, "bonus": 1000.50})
Smith.get_full_name()
Smith.get_total_income()