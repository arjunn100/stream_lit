import streamlit as st
import pandas as pd

# Initialize the session state for storing data
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Date", "Category", "Score"])

# Set up the Streamlit app
st.title("Progress Tracker")

# Sidebar for selecting the type of progress to track
option = st.sidebar.selectbox("Select Progress Type", 
                              ["Academics", "Football Matches", "Gym Workouts"])

# Input form for adding a new record
st.subheader(f"Add New {option} Record")
date = st.date_input("Date")
score = st.number_input("Score (out of 10)", min_value=0.0, max_value=10.0, step=0.1)
if st.button("Add Record"):
    new_record = {"Date": date, "Category": option, "Score": score}
    st.session_state.data = pd.concat([st.session_state.data, pd.DataFrame([new_record])], ignore_index=True)
    st.success(f"New {option} record added!")

# Display the records for the selected category
st.subheader(f"{option} Progress")
df = st.session_state.data[st.session_state.data["Category"] == option]

if not df.empty:
    df = df.sort_values(by="Date")
    st.dataframe(df)
    st.line_chart(df.set_index("Date")["Score"])
else:
    st.write(f"No records for {option} yet.")

# Option to reset all data
if st.sidebar.button("Reset All Data"):
    st.session_state.data = pd.DataFrame(columns=["Date", "Category", "Score"])
    st.success("All data has been reset!")
