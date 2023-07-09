from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel

'''доработайте базовый класс base.Vehicle:

добавьте атрибуты weight, started, fuel, fuel_consumption со значениями по умолчанию

добавьте инициализатор для установки weight, fuel, fuel_consumption

добавьте метод start. При вызове этого метода необходимо проверить состояние started.
И если не started, то нужно проверить, что топлива больше нуля, и обновить состояние started, 
иначе нужно выкинуть исключение exceptions.LowFuelError

добавьте метод move, который проверяет, что топлива достаточно для преодоления переданной дистанции 
(вплоть до полного расхода), и изменяет количество оставшегося топлива, 
иначе выкидывает исключение exceptions.NotEnoughFuel'''

class Vehicle(ABC):
    # weight = 1000
    # started = False
    # fuel = 45
    # fuel_consumption = 0.07
    #
    # def __init__(self, weight, fuel, fuel_consumption):
    #     self.weight = weight
    #     self.fuel = fuel
    #     self.fuel_consumption = fuel_consumption

    def __init__(self, weight = 1000, fuel = 45, fuel_consumption = 0.07, started = False):
        self.started = started
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started == True:
            return
        elif self.fuel > 0:
            self.started = True
        else:
            raise LowFuelError


    def move(self,	distance = 450):
        if self.fuel - distance * self.fuel_consumption > 0:
            self.fuel -= distance * self.fuel_consumption
        else:
            raise NotEnoughFuel


