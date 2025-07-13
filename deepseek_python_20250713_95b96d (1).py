import streamlit as st

def user_input_form():
    with st.form("health_form"):
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Age", min_value=1, max_value=100, value=25)
        with col2:
            gender = st.selectbox("Gender", ["Female", "Male", "Other"])
        
        days = st.slider("Days per week for health focus:", 1, 7, 3)
        health_issues = st.text_input("Any specific health concerns? (optional)")
        
        submitted = st.form_submit_button("Generate My Plan")
        
        if submitted:
            st.session_state.submitted = True
            return age, gender, days, health_issues
    return None, None, None, None