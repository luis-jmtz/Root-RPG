import pandas as pd

class Manuever():
    def __init__(self):
        self.type = 0 # offensive, defensive, or utility
        self.fp_cost = 0 # some manuevers have a focus point cost
        self.ap_cost = 0 # all manuevers have some AP cost
        self.pp = 0 # manuever power points
        self.description = "" # description