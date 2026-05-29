"""
PharmAI Assistant - Main Streamlit Application
An AI-powered personalized drug information assistant.
Users create accounts with medical profiles and receive AI-generated medication guidance.
"""

import streamlit as st
from utils.session_manager import init_session_state, is_logged_in, get_current_user, set_logged_in, logout
from ui.styles import apply_custom_styling
from ui.sidebar import render_sidebar
from ui.history import render_query_history
from main import handle_login, handle_signup, handle_medication_query, get_user_history
from database.mongodb import connect_to_mongodb, init_collections

# Page configuration
st.set_page_config(
    page_title="PharmAI Assistant",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom styling
apply_custom_styling()

# Initialize session state
init_session_state()

# Initialize database
@st.cache_resource
def init_db():
    """Initialize MongoDB connection (cached)"""
    connect_to_mongodb()
    init_collections()

init_db()

# Main app logic
def main():
    """Main application entry point"""
    
    # Check if user is logged in
    if not is_logged_in():
        # Display authentication page
        show_auth_page()
    else:
        # Display main dashboard
        show_dashboard()

def show_auth_page():
    """Display login/signup authentication page"""
    
    # Center content
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("<h1 style='text-align: center; color: #1f77b4;'>💊 PharmAI Assistant</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #666; font-size: 1.1rem;'>Your Personal AI-Powered Medication Guide</p>", unsafe_allow_html=True)
        st.markdown("---")
        
        # Create tabs for login and signup
        tab1, tab2 = st.tabs(["🔐 Login", "📝 Sign Up"])
        
        # LOGIN TAB
        with tab1:
            st.markdown("### Login to Your Account")
            
            login_email = st.text_input(
                "Email Address",
                key="login_email",
                placeholder="Enter your email"
            )
            
            login_password = st.text_input(
                "Password",
                type="password",
                key="login_password",
                placeholder="Enter your password"
            )
            
            if st.button("🔓 Login", use_container_width=True, key="login_btn"):
                if login_email and login_password:
                    success, user, error_msg = handle_login(login_email, login_password)
                    
                    if success:
                        set_logged_in(user)
                        st.success("✅ Login successful! Redirecting...")
                        st.rerun()
                    else:
                        st.error(f"❌ Login failed: {error_msg}")
                else:
                    st.warning("⚠️ Please fill in all fields")
            
            st.markdown("---")
            st.markdown("**Don't have an account?** Create one in the Sign Up tab →")
        
        # SIGNUP TAB
        with tab2:
            st.markdown("### Create Your PharmAI Account")
            
            # Basic Information
            st.markdown("#### Basic Information")
            signup_name = st.text_input(
                "Full Name",
                key="signup_name",
                placeholder="Enter your full name"
            )
            
            signup_email = st.text_input(
                "Email Address",
                key="signup_email",
                placeholder="Enter your email"
            )
            
            signup_password = st.text_input(
                "Password",
                type="password",
                key="signup_password",
                placeholder="Minimum 6 characters"
            )
            
            signup_age = st.number_input(
                "Age",
                min_value=1,
                max_value=150,
                value=30,
                key="signup_age"
            )
            
            # Medical Profile
            st.markdown("#### Medical Profile")
            
            signup_allergies = st.text_input(
                "Known Allergies (comma-separated)",
                key="signup_allergies",
                placeholder="e.g., Penicillin, Aspirin, Shellfish"
            )
            
            signup_conditions = st.text_input(
                "Existing Medical Conditions (comma-separated)",
                key="signup_conditions",
                placeholder="e.g., Diabetes, Hypertension, Asthma"
            )
            
            signup_medications = st.text_input(
                "Current Medications (comma-separated)",
                key="signup_medications",
                placeholder="e.g., Metformin, Lisinopril"
            )
            
            if st.button("✅ Create Account", use_container_width=True, key="signup_btn"):
                if signup_name and signup_email and signup_password:
                    success, user, error_msg = handle_signup(
                        signup_name,
                        signup_email,
                        signup_password,
                        int(signup_age),
                        signup_allergies,
                        signup_conditions,
                        signup_medications
                    )
                    
                    if success:
                        set_logged_in(user)
                        st.success("✅ Account created successfully! Logging in...")
                        st.rerun()
                    else:
                        st.error(f"❌ Registration failed: {error_msg}")
                else:
                    st.warning("⚠️ Please fill in all required fields")
            
            st.markdown("---")
            st.markdown("**Already have an account?** Login in the Login tab ←")

def show_dashboard():
    """Display main application dashboard"""
    
    user = get_current_user()
    
    # Render sidebar
    render_sidebar(user)
    
    # Main content
    st.markdown("<h1 style='text-align: center;'>💊 PharmAI Assistant</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: #666;'>Welcome, **{user.get('name', 'User')}**! 👋</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Main content area
    st.markdown("### 🔍 Ask About Medications")
    st.markdown("*Get personalized medication information based on your medical profile*")
    
    # Query input
    query_text = st.text_area(
        "Ask a medication-related question:",
        placeholder="e.g., What are the side effects of aspirin? Is it safe with my current medications?",
        height=120,
        label_visibility="collapsed"
    )
    
    # Submit button
    col1, col2, col3 = st.columns([1, 1, 2])
    
    with col1:
        submit_btn = st.button("💬 Get AI Response", use_container_width=True, type="primary")
    
    with col2:
        clear_btn = st.button("🗑️ Clear", use_container_width=True)
    
    if clear_btn:
        st.session_state.query_submitted = False
        st.rerun()
    
    # Handle query submission
    if submit_btn:
        if query_text and query_text.strip():
            st.session_state.query_submitted = True
        else:
            st.warning("⚠️ Please enter a question")
    
    # Display response
    if st.session_state.query_submitted and query_text and query_text.strip():
        st.markdown("---")
        
        with st.spinner("🤖 PharmAI is analyzing your question..."):
            success, response, error_msg = handle_medication_query(user, query_text)
        
        if success:
            st.markdown("### 🎯 AI Response")
            st.markdown(response)
        else:
            st.error(f"❌ Error: {error_msg}")
    
    # Display query history
    st.markdown("---")
    history = get_user_history(user)
    render_query_history(history)

# Run main app
if __name__ == "__main__":
    main()
