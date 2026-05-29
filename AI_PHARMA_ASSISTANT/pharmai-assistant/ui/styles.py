"""
Custom CSS styling for the Streamlit application.
Provides professional medical assistant appearance.
"""

import streamlit as st

def get_custom_css():
    """
    Return custom CSS for professional styling.
    
    Returns:
        CSS string for Streamlit styling
    """
    css = """
    <style>
    /* Main container styling */
    .main {
        padding: 2rem;
        background-color: #f8f9fa;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        padding: 2rem 1rem;
    }
    
    /* Header styling */
    h1 {
        color: #1f77b4;
        font-weight: 700;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    h2 {
        color: #2c5aa0;
        font-weight: 600;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    
    h3 {
        color: #35689e;
        font-weight: 600;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #1f77b4;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
        transition: background-color 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #0d47a1;
    }
    
    /* Text area styling */
    .stTextArea textarea {
        border-radius: 5px;
        border: 2px solid #e0e0e0;
        padding: 1rem;
        font-size: 1rem;
    }
    
    .stTextArea textarea:focus {
        border-color: #1f77b4;
        box-shadow: 0 0 0 3px rgba(31, 119, 180, 0.1);
    }
    
    /* Input field styling */
    .stTextInput input {
        border-radius: 5px;
        border: 2px solid #e0e0e0;
        padding: 0.75rem;
    }
    
    .stTextInput input:focus {
        border-color: #1f77b4;
        box-shadow: 0 0 0 3px rgba(31, 119, 180, 0.1);
    }
    
    /* Select box styling */
    .stSelectbox select {
        border-radius: 5px;
        border: 2px solid #e0e0e0;
        padding: 0.75rem;
    }
    
    /* Info boxes */
    .stInfo {
        background-color: #e3f2fd;
        border-left: 5px solid #1f77b4;
        border-radius: 5px;
    }
    
    .stWarning {
        background-color: #fff3e0;
        border-left: 5px solid #f57c00;
        border-radius: 5px;
    }
    
    .stError {
        background-color: #ffebee;
        border-left: 5px solid #c62828;
        border-radius: 5px;
    }
    
    .stSuccess {
        background-color: #e8f5e9;
        border-left: 5px solid #2e7d32;
        border-radius: 5px;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #f5f5f5;
        border-radius: 5px;
    }
    
    /* Expander styling */
    .stExpander {
        border: 1px solid #e0e0e0;
        border-radius: 5px;
        background-color: #ffffff;
    }
    
    /* Divider styling */
    hr {
        border: 0;
        border-top: 2px solid #e0e0e0;
        margin: 1.5rem 0;
    }
    
    /* Responsive design */
    @media (max-width: 640px) {
        .main {
            padding: 1rem;
        }
        
        [data-testid="stSidebar"] {
            padding: 1rem 0.5rem;
        }
        
        h1 {
            font-size: 1.5rem;
        }
        
        h2 {
            font-size: 1.25rem;
        }
    }
    </style>
    """
    return css

def apply_custom_styling():
    """
    Apply custom CSS styling to Streamlit app.
    Should be called at the start of app.py
    """
    st_css = get_custom_css()
    st.markdown(st_css, unsafe_allow_html=True)
