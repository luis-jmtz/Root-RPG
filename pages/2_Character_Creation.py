import streamlit as st


cc_path = r"Rules_Text\Character_Creation.md"

with open(cc_path, 'r', encoding='utf-8') as f:
    cc_text = f.read()

st.markdown(cc_text)