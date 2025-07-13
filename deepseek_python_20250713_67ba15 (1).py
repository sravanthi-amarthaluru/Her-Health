import streamlit as st
from components.header import show_header
from components.form import user_input_form
from components.cards import show_recommendations

def main():
    show_header()
    age, gender, days, health_issues = user_input_form()
    
    if st.session_state.get("submitted"):
        show_recommendations(age, gender, days, health_issues)

if __name__ == "__main__":
    main()