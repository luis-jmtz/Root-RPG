import streamlit as st
import pandas as pd
import os

# rules text files for Python
# core_path = r"Rules_Text\Core_Rules.md"
# condition_path = r"Rules_Text\Conditions.md"
# equip_path = r"Rules_Text\Equipment_Rules.md"
# skills_path = r"Rules_Text\Skills.md"

# for deployed app
from pathlib import Path

# Get the directory where your script is located
current_dir = Path(__file__).parent




# ------------------------------

# Get the directory where your script is located
current_dir = Path(__file__).parent

# Debug: Print current directory and check if files exist
st.write(f"Current directory: {current_dir}")
st.write(f"Files in current directory: {list(current_dir.glob('*'))}")
st.write(f"Files in Rules_Text folder: {list(current_dir.glob('Rules_Text/*'))}")

# Converted paths
core_path = current_dir / 'Rules_Text' / 'Core_Rules.md'
condition_path = current_dir / 'Rules_Text' / 'Conditions.md'
equip_path = current_dir / 'Rules_Text' / 'Equipment_Rules.md'
skills_path = current_dir / 'Rules_Text' / 'Skills.md'

# Debug: Print the actual paths
st.write(f"Core path: {core_path}")
st.write(f"Does core path exist? {core_path.exists()}")




# ---------------------





# --------------------------- opens rules text --------------- #
# Load files into session state if not already loaded
if 'core_rules' not in st.session_state:
    with open(core_path, 'r', encoding='utf-8') as f:
        st.session_state.core_rules = f.read()

if 'conditions' not in st.session_state:
    with open(condition_path, 'r', encoding='utf-8') as f:
        st.session_state.conditions = f.read()

if 'equip_rules' not in st.session_state:
    with open(equip_path, 'r', encoding='utf-8') as f:
        st.session_state.equip_rules = f.read()

if 'skill_rules' not in st.session_state:
    with open(skills_path, 'r', encoding='utf-8') as f:
        st.session_state.skill_rules = f.read()

# Create local variable references for convenient access
core_rules = st.session_state.core_rules
conditions = st.session_state.conditions
equip_rules = st.session_state.equip_rules
skill_rules = st.session_state.skill_rules


# ------------------ Combat Rules -------------------------- #


def load_markdown_files(folder_path):
    """Load all markdown files from a folder and return list of strings"""
    markdown_texts = []
    
    # Check if folder exists
    if not os.path.exists(folder_path):
        return markdown_texts
    
    # Get all .md files
    md_files = [f for f in os.listdir(folder_path) if f.endswith('.md')]
    # add a file for every file in the folder directory if ti ends with .md
    
    # Read each file
    for filename in md_files:
        file_path = os.path.join(folder_path, filename)
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                markdown_texts.append(content)
        except Exception as e:
            st.error(f"Error reading {filename}: {e}")
    
    return markdown_texts

combat_folder = r"Rules_Text\Combat_Rules"


if 'combat' not in st.session_state:
    st.session_state.combat = load_markdown_files(combat_folder)

combat_rules = st.session_state.combat




# -------------------- dataframe loading -------------------

if 'armor_df' not in st.session_state:
    st.session_state.armor_df = pd.read_csv(r"Data\armor.tsv", sep="\t")
armors = st.session_state.armor_df

if 'weapons_df' not in st.session_state:
    st.session_state.weapons_df = pd.read_csv(r"Data\weapons.tsv", sep="\t")
weapons = st.session_state.weapons_df

if 'properties_df' not in st.session_state:
    st.session_state.properties_df = pd.read_csv(r"Data\weapon_properties.tsv", sep="\t")
properties = st.session_state.properties_df

if 'shield_df' not in st.session_state:
    st.session_state.shield_df = pd.read_csv(r"Data\shields.tsv", sep="\t")
shields = st.session_state.shield_df

if 'basic_df' not in st.session_state:
    st.session_state.basic_df = pd.read_csv(r"Data\basic_equipment.tsv", sep="\t")
basic = st.session_state.basic_df





# ---------------- Actual UI Code ---------------------- #

st.title("Maplewood: an Oakhearth Spinoff")


tabs = ["Core Rules", "Equipment", "Conditions", "Combat","Skills"]

p1, p2, p3, p4,p5 = st.tabs(tabs)

# Core Rules
with p1:
    st.markdown(core_rules)

# Equipment
with p2:
    st.title("Equipment")

    st.markdown(equip_rules)

    # armors
    st.markdown("### Armor")
    armor_drops = ['id', 'pp']
    armors = armors.drop(armor_drops, axis=1)

    armors['type'] = armors['type'].replace({0: 'light', 1: 'heavy'})
    armors['stealth_dis'] = armors['stealth_dis'].replace({0: 'No', 1: 'Yes'})

    armors = armors.drop(index=0)

    # armors = armors.to_markdown(index=False)
    
    with st.expander("Armor List"):
        st.markdown(armors.to_markdown(index=False))

    st.write("Damage Resistance (dmg_resistance) reduces the amount of damage you take from Physical Damgage Sources (Bludgeoning, Piercing, Slashing) by the amount shown in the column.")
    

    # weapons
    st.markdown("### Weapons")
    
    weapon_drops = ["id", 'pp']
    weapons = weapons.drop(weapon_drops, axis=1)
    weapons['weapon_type'] = weapons['weapon_type'].replace({0: 'Melee', 1: 'Ranged'})
    weapons['ammo_type'] = weapons['ammo_type'].replace({0: 'None', 1: 'Arrow', 2: "Bolt", 3: "Bullet", 4: "Any Rock"})

    with st.expander("Weapon List"):
        # st.dataframe(weapons)
        st.markdown(weapons.to_markdown(index=False))

    st.markdown("#### Weapon Properties")
    properties = properties.drop("pp", axis=1)

    with st.expander("Weapon Properties List"):
        st.markdown(properties.to_markdown(index=False))


    st.markdown("### Shields")

    shields = shields.drop(weapon_drops, axis=1)
    shields['type'] = shields['type'].replace({0: 'light', 1: 'heavy'})

    with st.expander("Shield List"):
        st.markdown(shields.to_markdown(index=False))

    st.markdown("**Hit Points**: When you would take damage from an Attack, you can choose for your shield to take the damage instead. If your shield would be reduced to 0 hit points, it is destroyed.")

    st.markdown("While wielding a Shield, you can make an Unarmed Attack using the Shield.")

    st.markdown("### General Equipment")
    
    basic = basic.drop(weapon_drops, axis=1)

    with st.expander("List of General Equipment"):
        st.markdown(basic.to_markdown(index=False))



# Conditions
with p3:
    st.markdown(conditions)


# Combat Rules
with p4:
    st.title("Combat Rules")

    with st.expander("Core Combat Rules"):
        st.markdown(combat_rules[0])
        st.markdown(combat_rules[1])

    st.markdown("### Offensive Actions")

    with st.expander("List of Offensive Actions"):
        st.markdown(combat_rules[2])

    st.markdown("### Defensive Actions")

    with st.expander("List of Defensive Actions"):
        st.markdown(combat_rules[3])
    
    st.markdown("### Help, Held, and Move Actions")

    with st.expander("Help, Held, and Move Actions"):
        st.markdown(combat_rules[4])

    st.markdown("Reaction Rules")

    with st.expander("Reactions and Attacks of Opportunity"):
        st.markdown(combat_rules[5])

    st.markdown('### Misc Combat Rules')

    with st.expander("List of Miscellaneous Combat Rules"):
        st.markdown(combat_rules[6])

# Conditions
with p5:
    st.title("Skills")
    st.markdown(skill_rules)