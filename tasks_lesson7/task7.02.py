from abc import ABC, abstractmethod
class Clothes:


    @abstractmethod
    def calc(self):
        pass


class Coat(Clothes):
    v: float

    def __init__(self, v):
        self.v = v

    @property
    def calc(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    h: float

    def __init__(self, h):
        self.h = h

    @property
    def calc(self):
        return self.h * 2 + 0.3


coat = Coat(10)
suit = Suit(3)

print(f'Общий расход ткани: {round((coat.calc + suit.calc), 2)}')