import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set up the Streamlit app
st.title("Progress Tracker")

# Initialize or load data
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Date", "Category", "Score"])

# Sidebar for navigation
option = st.sidebar.selectbox("Select the type of progress to track:", 
                              ["Academics", "Football Matches", "Gym Workouts"])

# Input form for adding records
st.subheader(f"Add a new {option} record")
date = st.date_input("Date")
score = st.number_input("Score/Rating (out of 10)", min_value=0.0, max_value=10.0, step=0.1)
if st.button("Add Record"):
    new_record = {"Date": date, "Category": option, "Score": score}
    st.session_state.data = st.session_state.data.append(new_record, ignore_index=True)
    st.success("Record added successfully!")

# Display data and plots
st.subheader(f"{option} Progress")
df = st.session_state.data[st.session_state.data["Category"] == option]

if not df.empty:
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values(by="Date")
    st.dataframe(df)
    st.line_chart(df.set_index("Date")["Score"])
else:
    st.write("No data available for this category.")

# Option to reset data
if st.sidebar.button("Reset Data"):
    st.session_state.data = pd.DataFrame(columns=["Date", "Category", "Score"])
    st.success("Data reset successfully!")
