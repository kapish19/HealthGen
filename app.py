import streamlit as st
import webbrowser

# Set page config (now with HealthGen name)
st.set_page_config(
    page_title="HealthGen",
    page_icon="🏥",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': "### HealthGen - Bridging Healthcare Accessibility Gaps"
    }
)

# Custom CSS for styling (with reduced negative spacing)
st.markdown("""
    <style>
    .stApp {
        background-color: #f5f9ff;
        padding-top: 1rem;
    }
    .header {
        font-size: 36px;
        color: #2b5876;
        font-weight: 700;
        margin-bottom: 10px;  /* Reduced from 20px */
        text-align: center;
    }
    .subheader {
        font-size: 18px;
        color: #4e7c9f;
        margin-bottom: 20px;  /* Reduced from 30px */
        text-align: center;
    }
    .feature-card {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 15px;  /* Reduced from 20px */
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .feature-title {
        font-size: 20px;
        color: #2b5876;
        font-weight: 600;
        margin-bottom: 8px;  /* Reduced from 10px */
    }
    .feature-desc {
        font-size: 14px;
        color: #5a5a5a;
        margin-bottom: 0;
    }
    .stButton>button {
        background-color: #4e7c9f;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: 600;
        margin: 0 auto;
        display: block;
    }
    .stButton>button:hover {
        background-color: #3a5f7d;
        color: white;
    }
    .button-container {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-bottom: 20px;  /* Reduced from 30px */
    }
    /* Reduce spacing around horizontal rule */
    .stMarkdown hr {
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# URLs for redirection
ROUTE_URL = "https://hospitaldetector.streamlit.app/"
FORM_URL = "https://atuqmy2wd5h8zetufyd4vm.streamlit.app/"
VACCINE_URL = "https://kapish19-vaccination-reminder-bot-interfaceapp-dip7fp.streamlit.app/"

# Main content
st.markdown('<div class="header">HealthGen</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Bridging healthcare accessibility gaps through smart location mapping and AI-powered assistance</div>', unsafe_allow_html=True)

# Centered buttons container
st.markdown('<div class="button-container">', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Route Optimizer"):
        webbrowser.open_new_tab(ROUTE_URL)
with col2:
    if st.button("Medical Form Filler"):
        webbrowser.open_new_tab(FORM_URL)
with col3:
    if st.button("Vaccination Assistant"):
        webbrowser.open_new_tab(VACCINE_URL)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# Features section
st.markdown("## Our Features")

features = st.columns(2)

with features[0]:
    with st.container():
        st.markdown('<div class="feature-card"><div class="feature-title">Health Center Mapping</div><div class="feature-desc">Identify and map areas lacking healthcare facilities to plan new centers.</div></div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="feature-card"><div class="feature-title">AI Chatbot Assistant</div><div class="feature-desc">Get help with form-filling and healthcare guidance through our intelligent chatbot.</div></div>', unsafe_allow_html=True)

with features[1]:
    with st.container():
        st.markdown('<div class="feature-card"><div class="feature-title">Appointment Booking</div><div class="feature-desc">Easily book medical appointments with automated form-filling assistance.</div></div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="feature-card"><div class="feature-title">Medication Reminders</div><div class="feature-desc">Never miss important medications or vaccinations with our reminder system.</div></div>', unsafe_allow_html=True)