import pandas as pd
import math

class Creature():
    def __init__(self):
        self.level = 0
        self.combat_prof = 1 + math.floor(0.5 * self.level)

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

        # calculated values
        self.hit_points = 0 # for the moment assume the range is 0 to 20
        self.ac = 8 # 8 is the base value, AC = 8 + combat_prof + dexterity + armor bonus
        self.attack_bonus = 0 # combat_prof + Prime

        



