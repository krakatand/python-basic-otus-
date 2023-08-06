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
    #weight = 0
    #fuel = 0
    #fuel_consumption = 0
    #started = False
    #
    # def __init__(self, weight, fuel, fuel_consumption):
    #     self.weight = weight
    #     self.fuel = fuel
    #     self.fuel_consumption = fuel_consumption

    def __init__(self, weight=0, fuel=0, fuel_consumption=0,started=False):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

    def start(self):
        if self.started == True:
            return self.started
        elif self.fuel > 0:
            self.started = True
            return self.started
        else:
            raise LowFuelError


    def move(self,	distance = 450):
        if self.fuel - distance * self.fuel_consumption >= 0:
            self.fuel -= distance * self.fuel_consumption
            return self.fuel
        else:
            raise NotEnoughFuel


