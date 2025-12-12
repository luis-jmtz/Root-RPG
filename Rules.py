import streamlit as st
import pandas as pd

# rules text files
core_path = r"Rules_Text\Core_Rules.md"
condition_path = r"Rules_Text\Conditions.md"


# opens rules text
with open(core_path, 'r', encoding='utf-8') as f:
        # Read the entire contents into a single string variable
        core_rules = f.read()

with open(condition_path, 'r', encoding='utf-8') as f:
        # Read the entire contents into a single string variable
        conditions = f.read()

# dataframe loading

if 'armor_df' not in st.session_state:
    st.session_state.armor_df = pd.read_csv(r"Data\armor.tsv", sep="\t")
armors = st.session_state.armor_df

# st.markdown(core_rules)

st.title("Maplewood: an Oakhearth Spinoff")

tabs = ["Core Rules", "Equipment", "Conditions"]

p1, p2,p3 = st.tabs(tabs)

with p1:
        st.markdown(core_rules)

with p2:
        st.title("Equipment")

        # armors
        st.markdown("### Armor")
        armor_drops = ['id', 'pp']
        armors = armors.drop(armor_drops, axis=1)

        armors['type'] = armors['type'].replace({0: 'light', 1: 'heavy'})
        armors['stealth_dis'] = armors['stealth_dis'].replace({0: 'No', 1: 'Yes'})

        armors = armors.drop(index=0)

        # armors = armors.to_markdown(index=False)
        
        st.markdown(armors.to_markdown(index=False))

        st.write("Damage Reduction (dmg_reduction) reduces the amount of damage you take from Physical Damgage Sources (Bludgeoning, Piercing, Slashing) by the amount shown in the column")


with p3:
        st.markdown(conditions)