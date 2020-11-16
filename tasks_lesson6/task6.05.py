class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки ручкой")

class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки карандашом")

class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки маркером")

pen = Pen("ручка")
pencil = Pencil("карандаш")
marker = Handle("маркер")

pen.draw()
pencil.draw()
marker.draw()