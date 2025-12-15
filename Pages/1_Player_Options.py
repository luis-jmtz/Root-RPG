import streamlit as st
import pandas as pd

st.title("Player Options")

# --------------- load dataframes into session state --------------- #

if 'species_ids' not in st.session_state:
    st.session_state.species_ids = pd.read_csv(r"Data\species_list.tsv", sep="\t")
    st.session_state.species_list = st.session_state.species_ids['name'].to_list()

species_ids = st.session_state.species_ids
species_list = st.session_state.species_list

if 'species_abilities' not in st.session_state:
    st.session_state.species_abilities = pd.read_csv(r"Data\species_abilities.tsv", sep="\t")
    st.session_state.species_abilities = st.session_state.species_abilities.drop(["pp", "id"],axis=1)

species_abilities = st.session_state.species_abilities




# initialize tabs
tab_names = ["Species", "Player Classes"]
t1,t2 = st.tabs(tab_names)

with t1:

    for species in species_list:
        st.markdown(f"### {species}")
        temp_species_id = species_ids[species_ids["name"] == species].iloc[0,0]
        # st.markdown(temp_species_id)

        temp_df = species_abilities[species_abilities["species_id"] == temp_species_id].drop("species_id", axis=1)

        
        with st.expander(f"{species} Details:"):
            for row in temp_df.itertuples():
                st.markdown(f"**{row.name}**: {row.description}")
                # st.markdown(f"{row.description}")