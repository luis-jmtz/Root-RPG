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
    min_value=float(min_val),
    max_value=float(max_val),
    value=float((min_val + max_val) / 2),
    step=0.1
)

# Min-max scaling function
def min_max_scale(value, min_val, max_val):
    """Scale value to 0-1 range using min-max scaling"""
    if max_val == min_val:
        return 0.5  # Avoid division by zero
    return (value - min_val) / (max_val - min_val)

# Calculate scaled value
if min_val != max_val:
    scaled_value = min_max_scale(input_value, min_val, max_val)
    
    st.success(f"**Scaled value:** {scaled_value:.4f}")
    
    # Optional: Show the calculation
    with st.expander("Show calculation"):
        st.write(f"Formula: (value - min) / (max - min)")
        st.write(f"Calculation: ({input_value} - {min_val}) / ({max_val} - {min_val}) = {scaled_value:.4f}")
    
    # Impact analysis section
    st.subheader("Impact Analysis")
    
    change_amount = st.number_input(
        "Enter change amount to analyze:",
        value=1.0,
        step=0.1,
        help="How much to add/subtract from the current value to see the impact on scaled score"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Calculate impact of increasing
        new_value_increase = min(max_val, input_value + change_amount)
        new_scaled_increase = min_max_scale(new_value_increase, min_val, max_val)
        scaled_change_increase = new_scaled_increase - scaled_value
        
        st.metric(
            label=f"Adding {change_amount} to {selected_target}",
            value=f"{new_scaled_increase:.4f}",
            delta=f"+{scaled_change_increase:.4f}",
            help=f"New value: {new_value_increase}"
        )
    
    with col2:
        # Calculate impact of decreasing
        new_value_decrease = max(min_val, input_value - change_amount)
        new_scaled_decrease = min_max_scale(new_value_decrease, min_val, max_val)
        scaled_change_decrease = new_scaled_decrease - scaled_value
        
        st.metric(
            label=f"Subtracting {change_amount} from {selected_target}",
            value=f"{new_scaled_decrease:.4f}",
            delta=f"{scaled_change_decrease:.4f}",
            help=f"New value: {new_value_decrease}"
        )
    
    # Show the scaling factor
    scaling_factor = 1 / (max_val - min_val)
    st.info(f"**Scaling factor:** 1 unit of {selected_target} = {scaling_factor:.4f} scaled units")

else:
    st.error("Min and max values cannot be the same!")

# Display the reference table
st.subheader("Value Ranges Reference")
st.dataframe(df, use_container_width=True)