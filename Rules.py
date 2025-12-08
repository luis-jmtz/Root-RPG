import streamlit as st


core_path = r"Rules_Text\Core_Rules.md"
condition_path = r"Rules_Text\Conditions.md"

with open(core_path, 'r', encoding='utf-8') as f:
        # Read the entire contents into a single string variable
        core_rules = f.read()

with open(condition_path, 'r', encoding='utf-8') as f:
        # Read the entire contents into a single string variable
        conditions = f.read()


# st.markdown(core_rules)

st.title("Maplewood: an Oakhearth Spinoff")

tabs = ["Core Rules", "Conditions"]

p1, p2 = st.tabs(tabs)

with p1:
        st.markdown(core_rules)

with p2:
        st.markdown(conditions)