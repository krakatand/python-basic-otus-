"""
создайте датакласс Engine в модуле engine, добавьте атрибуты volume и pistons
"""

from dataclasses import dataclass


@dataclass
class Engine:
    volume: int
    pistons: int

    def __init__(self, volume, pistons):
        self.volume = volume
        self.pistons = pistons


