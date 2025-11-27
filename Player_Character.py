from Creatures import Creature

class Player_Character(Creature):
    def __init__(self):
        super().__init__()
        self.pc_class = 0 # id of player class
        self.species = 0 # id of player species
        self.vitality = 0 # effectively extra health a player character has after their hit_points have been depleted
        
        self.skill_points = 0
        self.expertise_points = 0
        self.skills = None # a dataframe that stores player skill information

        self.inventory = [] # a list of equipment a player holds
