"""
Session state management for Streamlit.
Handles initialization and management of session variables.
"""

import streamlit as st

def init_session_state():
    """
    Initialize Streamlit session state variables.
    Should be called at app startup.
    """
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    
    if 'user' not in st.session_state:
        st.session_state.user = None
    
    if 'query_submitted' not in st.session_state:
        st.session_state.query_submitted = False

def set_logged_in(user):
    """
    Set user as logged in and store user object.
    
    Args:
        user: User object from database
    """
    st.session_state.logged_in = True
    st.session_state.user = user

def logout():
    """
    Clear session state for logout.
    """
    st.session_state.logged_in = False
    st.session_state.user = None
    st.session_state.query_submitted = False

def is_logged_in():
    """
    Check if user is currently logged in.
    
    Returns:
        Boolean indicating login status
    """
    return st.session_state.get('logged_in', False)

def get_current_user():
    """
    Get currently logged in user.
    
    Returns:
        User object or None if not logged in
    """
    return st.session_state.get('user', None)
