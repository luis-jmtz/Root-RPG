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

if 'quirks_list' not in st.session_state:
    st.session_state.quirks_list = pd.read_csv(r"Data\quirks.tsv", sep="\t")
quirks_list = st.session_state.quirks_list



quirks_path = r"Rules_Text\Quirks.md"

if 'quirks_string' not in st.session_state:
    with open(quirks_path, 'r', encoding='utf-8') as f:
        st.session_state.quirks_string = f.read()

quirks_string = st.session_state.quirks_string



# initialize tabs
tab_names = ["Species", "Player Classes", "Quirks","Feats"]
t1,t2,t3,t4 = st.tabs(tab_names)

# Species
with t1:

    st.markdown("The Species options are purposely left vague to allow you to choose which and flavor any animal of your choice (within reason). You cannot play an animal any bigger than a normal wolf.")

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


# Player Classes
with t2:

    for pc_class in class_list:
        st.markdown(f"### {pc_class}")

        # paths to files and creates relevant dataframes
        base_features_path = rf"Data\PC_Class_Data\{pc_class}\{pc_class}.tsv"
        base_features_df = pd.read_csv(base_features_path, sep="\t")

        class_table_path = fr"Data\PC_Class_Data\{pc_class}\{pc_class}_table.tsv"
        class_table = pd.read_csv(class_table_path, sep="\t").to_markdown(index=False)

        
        subclass_ids_path = rf"Data\PC_Class_Data\{pc_class}\{pc_class}_subclass_id.tsv"
        subclass_id_df = pd.read_csv(subclass_ids_path, sep="\t")
        subclass_names = subclass_id_df["subclass"].to_list()

        subclass_data_path = rf"Data\PC_Class_Data\{pc_class}\{pc_class}_subclass_abilities.tsv"
        subclass_abilities = pd.read_csv(subclass_data_path, sep="\t").drop(["id","pp"], axis=1)

        # st.table(subclass_abilities)


        # data from the core class abilities
        base_features_df =  base_features_df.drop(["pp", 'id'], axis=1)

        proficiencies = base_features_df[base_features_df["level"] == 0]

        levels = range(1,6) # player levels go from 1 to 5

        with st.expander(f"{pc_class} Class Abilities"):

            st.markdown("##### Proficiencies")
            # loops to load the Proficiencies, separate from other abilities because it should go before the class table
            for row in proficiencies.itertuples():
                st.markdown(f"**{row.name}**: {row.description}")

            st.markdown(f"##### {pc_class} Class Table")
            st.markdown(class_table)

            st.markdown("##### Class Abilities")
            for n in levels:
                st.markdown(f"**Level {n}**")
                temp_df = base_features_df[base_features_df["level"] == n]


                for row in temp_df.itertuples():
                    description = str(row.description).replace(r'\\n', '\n')

                    st.markdown(f"*{row.name}*<br> {description}", unsafe_allow_html=True)

        with st.expander(f"{pc_class} Subclasses"):
            # st.markdown(subclass_names)
            for name in subclass_names:
                st.markdown(f"##### {name}")

                # get relevant subclass ID
                subclass_id = subclass_id_df[subclass_id_df["subclass"] == name].iloc[0, 0]

                # Get the subclass's abilities
                current_abilities = subclass_abilities[subclass_abilities["subclass"] == subclass_id]

                # groups abilities by level
                for level in sorted(current_abilities["level"].unique()):
                    level_abilities = current_abilities[current_abilities["level"] == level]

                    st.markdown(f"**Level {level}**")

                    for row in level_abilities.itertuples():
                        description = str(row.description).replace(r'\\n', '\n')
                        st.markdown(f"*{row.name}*<br> {description}", unsafe_allow_html=True)

# Quirks
with t3:
    st.markdown(quirks_string)
    max_species_id_value = max(species_ids["id"].to_list())

    quirks_species_range = range(0, max_species_id_value+1) # includes 0 for the quirks that are not species dependent

    # st.write(quirks_species_range)

    quirks_dfs = [] # list of dataframes. each dataframe will hold the quirks for a given species

    # adds the empty dataframes
    column_names = ['name', "requirements", "species_requirment", "description"]
    for species in quirks_species_range:
        quirks_dfs.append(pd.DataFrame(columns=column_names))

    # adds the correct quirks to the given dataframe
    for index, row in quirks_list.iterrows():
        # st.write(row)

        species_id = row['species_requirment']

        # Convert the row to a DataFrame and append it to the appropriate species dataframe
        row_df = pd.DataFrame([row])
        quirks_dfs[species_id] = pd.concat([quirks_dfs[species_id], row_df], ignore_index=True)

    # st.write(quirks_dfs)

    species_quirks_list = ["Generic", "Canine", "Feline", "Rodent", "Bird"]

    quirk_counter = 0

    for frame in quirks_dfs:

        st.write(f"### {species_quirks_list[quirk_counter]} Quirks")
        with st.expander(f"{species_quirks_list[quirk_counter]} Quirks"):
            for row in frame.itertuples():
                st.write(f"##### **{row.name}**")

                if row.requirements == "0":
                    st.write(f"*Requirements* - None")
                else:
                    st.write(f"*Requirements* - {row.requirements}")


                st.write(f"{row.description}")
                st.write("---")
        quirk_counter +=1
    



with t4:
    st.title("Feats")