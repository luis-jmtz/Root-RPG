import pandas as pd

class Equipment():
    def __init__(self):
        self.id = 0 # int, id of the equipment within its dataset
        self.name = ""
        self.description = ""
        self.value = 0 # currency is non standard, so value is a more vague and flexible quality
        self.pp = 0 # power points, represents how much much the object effect's a creature's difficulty

class Armor(Equipment):
    def __init__(self):
        super().__init__()

        self.ac = 0 # the bonus to armor class
        self.damge_reduction = 0 # some armor reduces damage taken
        self.dex_penality = 0 # some armor reduces dexterity bonus on rolls
        self.type = 0 # light or heavy armor, 0 = light, 1 = heavy

class Weapon(Equipment):
    def __init__(self):
        super().__init__()
        self.dmg = 0 # damage
        self.dmg_type = 0 # weapon's damage type
        self.range = 1 # how far can a weapon reach, default = 1 which means it hit anything within 1 space of it
        # not going to add effective and ineffective range for bows
        self.ammo_type = 0 # default = 0, if zero, no ammo is needed. 1 = arrows, 2 = bolts, 3 = bullet
        self.properties = "" # string that contains weapon's properties

class Shield(Equipment):
    def __init__(self):
        super().__init__()
        self.ac = 0 # shields can increase armor class
        self.hit_points = 0 # creatures can have their shield take damage for them


