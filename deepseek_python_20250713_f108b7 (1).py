import streamlit as st
from streamlit.components.v1 import html

# Initialize session state
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# Load CSS
def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# App Header
st.title("🏥 HerHealth+ Personalized Recommendations")

# Input Form
with st.form("health_form"):
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value=1, max_value=100, value=25)
    with col2:
        gender = st.selectbox("Gender", ["Female", "Male", "Other"])
    
    days = st.slider("Days per week for health focus:", 1, 7, 3)
    health_issues = st.text_input("Any specific health concerns? (optional)")
    
    if st.form_submit_button("Generate My Plan"):
        st.session_state.submitted = True

# Show Results
if st.session_state.submitted:
    st.success("Here's your personalized health plan!")
    
    # Hygiene Tips Card
    st.markdown("""
    <div class="card">
        <div class="card-header">🧼 Hygiene Tips</div>
        <div class="card-content">
            <ul>
                <li>Shower daily with mild soap.</li>
                <li>Wash hands frequently.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Add other cards here...