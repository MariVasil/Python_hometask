import time


class TrafficLight:
    __color: str

    def running(self):
        while True:
            self.__color = "красный"
            print(f"Свет светофора - {self.__color}")
            time.sleep(7)
            self.__color = "желтый"
            print(f"Свет светофора - {self.__color}")
            time.sleep(2)
            self.__color = "зелёный"
            print(f"Свет светофора - {self.__color}")
            time.sleep(9)


traffic_light = TrafficLight()
traffic_light.running()
