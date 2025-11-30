from Creatures import *
import pandas as pd
# import inspect



test = Creature()

test.add_basic_equipment(1)

print(test.inventory[0].__dict__)

# print(test.__dict__)