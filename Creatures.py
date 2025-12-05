import pandas as pd
import math
from Equipment import *

class Creature():
    def __init__(self):
        self.level = 0
        self.prof = 1 + math.floor(0.5 * self.level)

        # attributes, range between -5 and 5
        self.might = 0
        self.dex = 0
        self.intell = 0 #intelligence
        self.charisma = 0
        self.prime = max([self.might, self.dex, self.intell, self.charisma])

        # size and movement
        self.size = 0 # goes from -2 to 2, with 0 as the standard, size has no direct effect on abilities
        self.speed = 0 # base amount is 6, so the range is from 0 to 12
        self.fly_speed = 0 # default is 0, not displayed when 0
        self.burrow_speed = 0 # default is 0, not displayed when 0
        self.climb_speed = 0 # default is 0, not displayed when 0

        # combat
        self.ap = 2 # base amount for non-player creature is 2
        self.num_attacks = 1 # base amount for non-player creature is 1
        self.fp = 0 # focus points, default 0, if not zero creature gains access to Manuevers

        # equipment
        self.armor = None # custom armor objects
        self.shield = None # custom shield objects
        self.weapons = [] # list of weapons objects
        self.inventory = [] # list of objects a creature is holding
        self.abilities = [] # list of ability objects

        # calculated values
        self.hit_points = 0 # for the moment assume the range is 0 to 20
        self.ac = 8 # 8 is the base value, AC = 8 + prof + dexterity + armor bonus
        self.attack_bonus = 0 # prof + Prime

        self.dl = 0 # difficulty level: the sum of all of a creature's

    # -------- Calculate Bonuses and PP ------ #

    def calc_ac(self):
        # AC = 8 + Combat Proficiency + Dexterity + Armor + Shield + Misc
        temp_ac = 8 + self.prof + self.dex
        temp_pp = 0 # also get the pp from armor and shields, pp from abilities will be calculated separately
        
        calc_string = f"8 + prof({self.prof}) + dex({self.dex})"

        if self.armor != None:
            temp_ac += self.armor.ac
            calc_string += f" + armor({self.armor.ac})"
            temp_pp += self.armor.pp

        if self.shield != None:
            temp_ac += self.shield.ac
            calc_string += f" + shield({self.shield.ac})"
            temp_pp += self.shield.pp

        # ADDME - add AC from ability

        self.ac = temp_ac

        calc_string += f" = {self.ac}"
        # print(calc_string)
        # maybe return pp? later problem

        
    # ---------------- Add Equipment ----------------- #

    def add_basic_equipment(self,id): #adds to creature Inventory
        item = Equipment(id,0)
        self.inventory.append(item)

    def equip_armor(self, id):
        armor = Armor(id)
        self.armor = armor

    def add_weapon(self,id):
        weapon = Weapon(id)
        self.inventory.append(weapon)

    def equip_shield(self,id):
        shield = Shield(id)
        self.shield = shield