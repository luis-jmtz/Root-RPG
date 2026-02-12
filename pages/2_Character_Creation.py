import streamlit as st
from pathlib import Path


# cc_path = r"Rules_Text\Character_Creation.md"

# with open(cc_path, 'r', encoding='utf-8') as f:
#     cc_text = f.read()

# st.markdown(cc_text)



# Get the directory where this script is located
current_dir = Path(__file__).parent
# Go up one level to the root directory (since this file is in the pages folder)
root_dir = current_dir.parent

cc_path = root_dir / 'Rules_Text' / 'Character_Creation.md'

with open(cc_path, 'r', encoding='utf-8') as f:
    cc_text = f.read()

st.markdown(cc_text)