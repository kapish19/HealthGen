import streamlit as st

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

# Custom CSS for styling
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
        margin-bottom: 10px;
        text-align: center;
    }
    .subheader {
        font-size: 18px;
        color: #4e7c9f;
        margin-bottom: 20px;
        text-align: center;
    }
    .feature-card {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .feature-title {
        font-size: 20px;
        color: #2b5876;
        font-weight: 600;
        margin-bottom: 8px;
    }
    .feature-desc {
        font-size: 14px;
        color: #5a5a5a;
        margin-bottom: 0;
    }
    .button-container {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-bottom: 20px;
        flex-wrap: wrap;
    }
    .button-container a button {
        background-color: #4e7c9f;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: 600;
        cursor: pointer;
        font-size: 16px;
    }
    .button-container a button:hover {
        background-color: #3a5f7d;
    }
    .stMarkdown hr {
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Main content
st.markdown('<div class="header">HealthGen</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Bridging healthcare accessibility gaps through smart location mapping and AI-powered assistance</div>', unsafe_allow_html=True)

# Buttons using HTML for client-side navigation
st.markdown("""
<div class="button-container">
    <a href="https://hospitaldetector.streamlit.app/" target="_blank">
        <button>Route Optimizer</button>
    </a>
    <a href="https://atuqmy2wd5h8zetufyd4vm.streamlit.app/" target="_blank">
        <button>Medical Form Filler</button>
    </a>
    <a href="https://kapish19-vaccination-reminder-bot-interfaceapp-dip7fp.streamlit.app/" target="_blank">
        <button>Vaccination Assistant</button>
    </a>
</div>
""", unsafe_allow_html=True)

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
