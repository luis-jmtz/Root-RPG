from Creatures import *
import pandas as pd
# import inspect



# test = Creature()

# # test.add_basic_equipment(1)
# # test.add_weapon(1)

# print(pd.Series(test.__dict__), "\n\n")


# test.equip_armor(1)
# test.calc_ac()
# print(pd.Series(test.__dict__), "\n\n")


# test.equip_shield(1)
# test.calc_ac()
# print(pd.Series(test.__dict__), "\n\n")


# test.dex = 2
# test.calc_ac()
# print(pd.Series(test.__dict__), "\n\n")


# test.equip_armor(6)
# test.calc_ac()
# print(pd.Series(test.__dict__), "\n\n")


df = pd.read_csv(r"Data\quirks.tsv", sep="\t")
print(df.iloc[12])