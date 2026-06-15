import streamlit as st
from ai_engine import ask_ai

st.title("Study Genie AI")

option = st.selectbox(
    "Choose Feature",
    ["Doubt Solver", "Study Planner", "Quiz", "Motivation", "Career"]
)

user_input = st.text_input("Enter here")

if st.button("Submit"):
    output = ask_ai(user_input)
    st.write(output)
