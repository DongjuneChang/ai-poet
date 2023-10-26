import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json

# Function to download and parse JSON from a URL
def load_json_from_url(url):
    response = requests.get(url)
    return json.loads(response.content)

# Function to download CSV from a URL
def load_csv_from_url(url):
    response = requests.get(url)
    return pd.read_csv(response.content.decode('utf-8'))

def display_json_data(data):
    st.write("### Top Level Master ID")
    st.write(data["top_level_master_id"])
    
    st.write("### ROS Info Data")
    st.write(data["ros_info_data"])
    
    st.write("### Devices")
    for device in data["devices"]:
        st.write(device)
    
    st.write("### Device Groups")
    for group in data["device_groups"]:
        st.write(group)

st.title("Startup JSON Parser and CSV Loader")

# Load JSON from given URL
json_url = "https://drive.google.com/uc?export=download&id=1QR2QFl2VonhIDaUvOzvfW3ARb3JCoBqy"
data = load_json_from_url(json_url)

# Display JSON Data
display_json_data(data)

# Download and Display CSV from task_information_url
st.write("### Task Information CSV")
task_info_url = data["ros_info_data"]["task_information_url"]
df = load_csv_from_url(task_info_url)
st.write(df)

# Sidebar for filtering
st.sidebar.header("Filter options")
selected_exp = st.sidebar.selectbox("Choose Exp", df['Exp'].unique())
filtered_df = df[df['Exp'] == selected_exp]

# Display data
st.write(f"Displaying data for Exp: {selected_exp}")
st.write(filtered_df)

# Sort data
sort_option = st.selectbox("Sort by", df.columns)
sorted_df = filtered_df.sort_values(by=sort_option)
st.write(f"Sorted by {sort_option}")
st.write(sorted_df)

# Visualization
st.subheader("Visualization")
fig, ax = plt.subplots()
ax.scatter(sorted_df['targetx'], sorted_df['targety'])
ax.set_xlabel('Target X')
ax.set_ylabel('Target Y')
st.pyplot(fig)
