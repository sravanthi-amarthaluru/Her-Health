import streamlit as st

def show_recommendations(age, gender, days, health_issues):
    st.success("Here’s your personalized health plan!")
    
    # Hygiene Tips
    st.markdown("""
    <div class="card">
        <div class="card-header">🧼 Hygiene Tips</div>
        <div class="card-content">
            <ul>
                <li>Shower daily with mild soap.</li>
                <li>Wash hands frequently.</li>
                <li>Brush teeth twice a day.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Diet Plan (Add other cards similarly)
    st.markdown("""
    <div class="card">
        <div class="card-header">🍎 Diet Plan</div>
        <div class="card-content">
            <ul>
                <li>Eat fruits and vegetables.</li>
                <li>Drink 8 glasses of water.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)