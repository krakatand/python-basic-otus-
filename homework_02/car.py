"""
в модуле car создайте класс Car
класс Car должен быть наследником Vehicle

добавьте атрибут engine классу Car

объявите метод set_engine, который принимает в себя экземпляр объекта
Engine и устанавливает на текущий экземпляр Car
"""

from homework_02.base import Vehicle
from homework_02.engine import Engine

class Car(Vehicle):

    def __init__(self,weight=0, fuel=0, fuel_consumption=0, started=False, engine=(0,0)):
        super().__init__(weight=weight, fuel=fuel, fuel_consumption=fuel_consumption, started=started)
        self.engine = engine



    def set_engine(self, volume, pistons):
        self.engine = Engine(volume, pistons)

