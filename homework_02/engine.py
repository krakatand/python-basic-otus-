"""
создайте датакласс Engine в модуле engine, добавьте атрибуты volume и pistons
"""

from dataclasses import dataclass

@dataclass
class Engine:
    volume: str
    pistons: str