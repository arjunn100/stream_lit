import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set up the Streamlit app
st.title("Progress Tracker")

# Sidebar for navigation
option = st.sidebar.selectbox("Select the type of progress you want to track:", 
                              ["Academics", "Football Matches", "Gym Workouts"])

# Create an empty DataFrame to store progress data
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Date", "Category", "Score"])

# Function to add a new record
def add_record(date, category, score):
    new_data = pd.DataFrame({"Date": [date], "Category": [category], "Score": [score]})
    st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)
    st.success("Record added successfully!")

# Function to display data and plots
def display_data(category):
    df = st.session_state.data[st.session_state.data["Category"] == category]
    if not df.empty:
        st.write(f"### {category} Progress")
        st.dataframe(df)
        st.line_chart(df.set_index("Date")["Score"])
    else:
        st.write("No data available for this category.")

# Input form for adding records
with st.form("Add Record"):
    st.write(f"### Add a new {option} record")
    date = st.date_input("Date")
    score = st.number_input("Score/Rating (out of 10)", min_value=0.0, max_value=10.0, step=0.1)
    submitted = st.form_submit_button("Add Record")
    
    if submitted:
        add_record(date, option, score)

# Display data based on selected option
display_data(option)

# Option to reset data
if st.sidebar.button("Reset Data"):
    st.session_state.data = pd.DataFrame(columns=["Date", "Category", "Score"])
    st.success("Data reset successfully!")
