class OfficeEquipmentStorage:
    office_equip: dict

    def __init__(self):
        self.office_equip = {}

    def store(self, name, number):
        if self.office_equip.keys().__contains__(name):
            self.office_equip[name] += number
        else:
            self.office_equip[name] = number

    def transfer(self, dep, name, number):
        assert self.office_equip.keys().__contains__(name)
        stored = self.office_equip[name]
        assert stored >= number
        self.office_equip[name] -= number
        dep.store(name, number)

    def __str__(self):
        return  self.office_equip.__str__();


class OfficeDepartment:
    office_equip: dict

    def __init__(self):
        self.office_equip = {}

    def store(self, name, number):
        if self.office_equip.keys().__contains__(name):
            self.office_equip[name] += number
        else:
            self.office_equip[name] = number

    def __str__(self):
        return self.office_equip.__str__();


class OfficeEquipment:
    name: str

    def __init__(self, name):
        self.name = name


class Printer(OfficeEquipment):
    color_printer: bool
    printing_speed: int

    def __init__(self, name,  color, speed):
        super().__init__(name)
        self.color_printer = color
        self.printing_speed = speed


class Scaner(OfficeEquipment):
    wifi_connection: bool
    sensor_type: str

    def __init__(self, name, wifi, sensor):
        super().__init__(name)
        self.wifi_connection = wifi
        self.sensor_type = sensor


class Xerox(OfficeEquipment):
    speed: int
    resolution: int

    def __init__(self, name, speed, resolution):
        super().__init__(name)
        self.speed = speed
        self.resolution = resolution


xerox1 = Xerox("xer1", 1, 1)
printer1 = Printer("print1", True, 1)
storage1 = OfficeEquipmentStorage()
storage1.store(printer1.name, 1)
storage1.store(printer1.name, 1)
storage1.store(xerox1.name, 1)

print(storage1)

dep1 = OfficeDepartment()
storage1.transfer(dep1, "print1", 1)

print(storage1)
print(dep1)