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



if 'class_ids' not in st.session_state:
    st.session_state.class_ids =  pd.read_csv(r"Data\PC_Class_Data\class_id.tsv", sep="\t")
    st.session_state.class_list = st.session_state.class_ids['name'].to_list()

class_ids = st.session_state.class_ids
class_list = st.session_state.class_list




# initialize tabs
tab_names = ["Species", "Player Classes"]
t1,t2 = st.tabs(tab_names)

with t1:

    # loops through the species list and generates the display for each species
    for species in species_list:
        st.markdown(f"### {species}")
        temp_species_id = species_ids[species_ids["name"] == species].iloc[0,0]
        # st.markdown(temp_species_id)

        temp_df = species_abilities[species_abilities["species_id"] == temp_species_id].drop("species_id", axis=1)

        
        with st.expander(f"{species} Details:"):
            for row in temp_df.itertuples():
                st.markdown(f"**{row.name}**: {row.description}")
                # st.markdown(f"{row.description}")

with t2:

    for pc_class in class_list:
        st.markdown(f"### {pc_class}")

        base_features_path = rf"Data\PC_Class_Data\{pc_class}\{pc_class}.tsv"
        base_features_df = pd.read_csv(base_features_path, sep="\t")

        base_features_df =  base_features_df.drop(["pp", 'id'], axis=1)

        proficiencies = base_features_df[base_features_df["level"] == 0]

        # contains abilities that are not proficiencies
        abilities = base_features_df[~base_features_df['level'].isin(proficiencies['level'])]

        with st.expander(f"{pc_class} Class Abilities"):

            st.markdown("##### Proficiencies")
            # loops to load the Proficiencies, separate from other abilities because it should go before the class table
            for row in proficiencies.itertuples():
                st.markdown(f"**{row.name}**: {row.description}")

            


            # st.table(base_features_df)
