import streamlit as st
from ai_engine import ask_ai

st.title("StudyGenie AI")

user_input = st.text_input("Ask your question")

if st.button("Send"):
    if user_input.strip() != "":
        response = ask_ai(user_input)
        st.write(response)
    else:
        st.write("Please type something first.")
