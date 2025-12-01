from Creatures import *
import pandas as pd
# import inspect



test = Creature()

test.add_basic_equipment(1)
test.add_weapon(1)

print(test.inventory[1].__dict__)

test.equip_armor(1)

test.equip_shield(1)

print(test.shield.__dict__)

# print(test.__dict__)