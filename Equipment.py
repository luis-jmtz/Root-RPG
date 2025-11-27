import pandas as pd

class Equipment():
    def __init__(self):
        self.id = 0 # int, id of the equipment within its dataset
        self.value = 0 # currency is non standard, so value is a more vague and flexible quality
        self.pp = 0 # power points, represents how much much the object effect's a creature's difficulty

class Armor(Equipment):
    def __init__(self):
        super().__init__()

