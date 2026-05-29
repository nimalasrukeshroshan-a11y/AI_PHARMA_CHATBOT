"""
Sidebar UI component for displaying user profile and logout.
Shows user information and provides logout functionality.
"""

import streamlit as st

def render_sidebar(user):
    """
    Render the sidebar with user profile information.
    
    Args:
        user: User object containing profile information
    """
    with st.sidebar:
        st.markdown("---")
        st.markdown("### 👤 User Profile")
        st.markdown("---")
        
        # Display user information
        st.write(f"**Name:** {user.get('name', 'N/A')}")
        st.write(f"**Email:** {user.get('email', 'N/A')}")
        st.write(f"**Age:** {user.get('age', 'N/A')} years")
        
        st.markdown("---")
        st.markdown("### 🏥 Medical Profile")
        st.markdown("---")
        
        # Display allergies
        allergies = user.get('known_allergies', [])
        if allergies:
            st.write("**Known Allergies:**")
            for allergy in allergies:
                st.write(f"  • {allergy}")
        else:
            st.write("**Known Allergies:** None reported")
        
        # Display conditions
        conditions = user.get('existing_conditions', [])
        if conditions:
            st.write("**Existing Conditions:**")
            for condition in conditions:
                st.write(f"  • {condition}")
        else:
            st.write("**Existing Conditions:** None reported")
        
        # Display medications
        medications = user.get('current_medications', [])
        if medications:
            st.write("**Current Medications:**")
            for medication in medications:
                st.write(f"  • {medication}")
        else:
            st.write("**Current Medications:** None reported")
        
        st.markdown("---")
        
        # Logout button
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.user = None
            st.rerun()
