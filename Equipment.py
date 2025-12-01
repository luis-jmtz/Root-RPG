import pandas as pd

# data imports
basic_equipment = pd.read_csv(r"Data\basic_equipment.tsv",sep="\t")
armor = pd.read_csv(r"Data\armor.tsv",sep="\t")
shields = pd.read_csv(r"Data\shields.tsv",sep="\t")
weapons = pd.read_csv(r"Data\weapons.tsv",sep="\t")



# equipment types: 0 = basic, 1 = armor, 2 = Weapon, 3 = Shield

class Equipment():
    def __init__(self, id, equipment_type):
        self.id = id # int, id of the equipment within its dataset
        self.name = 0
        self.description = 0
        self.value = 0 # currency is non standard, so value is a more vague and flexible quality
        self.pp = 0 # power points, represents how much much the object effect's a creature's difficulty
        self.data = None

        self.set_values(equipment_type)

    def set_values(self, equipment_type):

        match equipment_type:
            case 0:
                dataset = basic_equipment
            case 1:
                dataset = armor
            case 2:
                dataset = weapons
            case 3:
                dataset = shields

        self.data = dataset[dataset["id"] == self.id].iloc[0] # returns a series with values

        self.name = self.data.get("name")
        self.description = self.data.get("description")
        self.value = self.data.get("value") # currency is non standard, so value is a more vague and flexible quality
        self.pp = self.data.get("pp") # power points, represents how much much the object effect's a creature's difficulty



class Armor(Equipment):
    def __init__(self,id):
        super().__init__(id, equipment_type=1)

        self.ac = 0 # the bonus to armor class
        self.damge_reduction = 0 # some armor reduces damage taken
        self.stealth_dis = 0 # some armor reduces dexterity bonus on rolls
        self.type = 0 # light or heavy armor, 0 = light, 1 = heavy
        self.set_armor_values()


    def set_armor_values(self):
        # Get the armor data for this specific armor ID
        self.ac = self.data.get("ac", 0)
        self.damage_reduction = self.data.get("damage_reduction", 0)
        self.stealth_dis = self.data.get("stealth_dis", 0)
        self.type = self.data.get("type", 0)


class Weapon(Equipment):
    def __init__(self, id):
        super().__init__(id, equipment_type=2)
        self.dmg = 0 # damage
        self.dmg_type = "" # weapon's damage type
        self.weapon_type = 0 # 0 is for melee, 1 is for ranged weapons
        self.range = 1 # how far can a weapon reach, default = 1 which means it hit anything within 1 space of it
        # not going to add effective and ineffective range for bows
        self.ammo_type = 0 # default = 0, if zero, no ammo is needed. 1 = arrows, 2 = bolts, 3 = bullet, 4 = rock
        self.properties = "" # string that contains weapon's properties


class Shield(Equipment):
    def __init__(self):
        super().__init__()
        self.ac = 0 # shields can increase armor class
        self.hit_points = 0 # creatures can have their shield take damage for them
        self.type = 0 # 0 = light shield, 1 = heavy shield


