from Creatures import Creature

class Vagabond(Creature):
    def __init__(self):
        super().__init__()
        self.pc_class = 0 # id of player class
        self.species = 0 # id of player species
        self.vitality = 0 # effectively extra health a player character has after their hit_points have been depleted

        self.equipment_proficiencies = [] # equipment proficiencies (abilities)
        
        self.skill_proficiencies = [] # list of skills (id) that a player character has proficiency in
        self.skills = None # a dataframe that stores player skill information

        self.quiver = [] # holds ammunition, only used when a player has a quiver
