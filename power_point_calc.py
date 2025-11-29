'''
this file will be used to calculate the amount of power points
an ability, manuever, or equipment provides.

All power points for a creature will be calculated to determine it Diffiuclty Level
'''


# creature difficulty score = base_pp + offensive_pp + defensive_pp + utility_pp


import streamlit as st
import pandas as pd

# Load the min-max values from your TSV file
df = pd.read_csv('pp_min_max.tsv', sep='\t')

# Streamlit app
st.title("Min-Max Scaler")
st.write("Convert values to normalized scale (0-1) based on their min-max ranges")

# Dropdown to select the target value type
selected_target = st.selectbox("Select value type:", df['target_value'].tolist())

# Get the min and max values for the selected target
min_val = df[df['target_value'] == selected_target]['min_value'].values[0]
max_val = df[df['target_value'] == selected_target]['max_value'].values[0]

st.write(f"**Range:** {min_val} to {max_val}")

# Input for the value to scale
input_value = st.number_input(
    f"Enter value for {selected_target}:",
    value=float((min_val + max_val) / 2),
    step=1.0
)

# Calculate scaling factor and scaled value
if max_val != min_val:
    scaling_factor = 1 / (max_val - min_val)
    scaled_value = input_value * scaling_factor
    
    st.success(f"**Scaling factor:** {scaling_factor:.4f}")
    st.success(f"**Scaled value:** {scaled_value:.4f}")
    
    with st.expander("Show calculation"):
        st.write(f"Formula: input_value × scaling_factor")
        st.write(f"Calculation: {input_value} × {scaling_factor:.4f} = {scaled_value:.4f}")
else:
    st.error("Min and max values cannot be the same!")

# Display the reference table
st.subheader("Value Ranges Reference")
st.dataframe(df, use_container_width=True)