import pandas as pd

class Ability():
    def __init__(self):
        self.id = 0 
        self.name = ""
        self.description = ""
        self.pp = 0 # how much the ability contributes to the creauture's difficulty

class Species_Trait(Ability):
    def __init__(self):
        super().__init__()
        self.species_id = 0 #species id

class Class_Ability(Ability):
    def __init__(self):
        super().__init__()
        self.class_id = 0