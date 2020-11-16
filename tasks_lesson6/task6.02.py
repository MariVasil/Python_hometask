class Road:
    _length: str
    _width: str

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def count_mass(self):
        mass = round((self._length * self._width * 25 * 5 / 1000),2)
        print(f"Масса асфальта, необходимая для покрытия всего дорожного полотна - {mass} т")


road = Road(20, 5000)
road.count_mass()
