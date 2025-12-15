import streamlit as st
import pandas as pd

st.title("Player Options")

# --------------- load dataframes into session state --------------- #

if 'species_list' not in st.session_state:
    st.session_state.species_list = pd.read_csv(r"Data\species_list.tsv", sep="\t")
species_list = st.session_state.species_list

if 'species_abilities' not in st.session_state:
    st.session_state.species_abilities = pd.read_csv(r"Data\species_abilities.tsv", sep="\t")
    st.session_state.species_abilities = st.session_state.species_abilities.drop(["pp", "id"],axis=1)

species_abilities = st.session_state.species_abilities




# initialize tabs
tab_names = ["Species", "Player Classes"]
t1,t2 = st.tabs(tab_names)

with t1:
    st.table(species_list)
    st.table(species_abilities)