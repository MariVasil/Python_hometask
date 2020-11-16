class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Автомобиль начал движение")

    def stop(self):
        print("Автомобиль остановился")

    def turn_direction(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        print(f"Скорость движения автомобиля - {self.speed}")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Скорость автомобиля превышает разрешённую")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Скорость автомобиля превышает разрешённую")


class PoliceCar(Car):
    pass


cars = [
    TownCar(50, "желтый", "toyota", False),
    TownCar(80, "красный", "ford", False),
    SportCar(100, "зелёный", "ferrari", False),
    WorkCar(40, "зелёный", "ford", False),
    WorkCar(55, "синий", "ford", False),
    PoliceCar(60, "белый", "suzuki", True)
    ]

for car in cars:
    print(f"Марка автомобиля - {car.name}, цвет автомобиля - {car.color}")
    car.go()
    car.stop()
    car.turn_direction("направо")
    car.turn_direction("налево")
    car.show_speed()
