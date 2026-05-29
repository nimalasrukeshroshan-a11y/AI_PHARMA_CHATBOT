"""
Query history display component.
Shows user's previous medication queries and AI responses.
"""

import streamlit as st
from datetime import datetime

def render_query_history(history):
    """
    Render the query history section with expandable items.
    
    Args:
        history: List of query history documents from MongoDB
    """
    if not history:
        st.info("📋 No query history yet. Ask your first question to get started!")
        return
    
    st.markdown("---")
    st.markdown("### 📋 Query History")
    st.markdown("*Last 10 queries shown below (newest first)*")
    
    for idx, item in enumerate(history, 1):
        # Format timestamp
        timestamp = item.get('timestamp', datetime.now())
        if isinstance(timestamp, str):
            time_str = timestamp
        else:
            time_str = timestamp.strftime("%B %d, %Y at %I:%M %p")
        
        # Create expander for each query
        with st.expander(
            f"**Query {idx}** - {time_str}",
            expanded=False
        ):
            st.markdown("#### Your Question:")
            st.write(item.get('query', 'N/A'))
            
            st.markdown("#### AI Response:")
            st.markdown(item.get('response', 'No response available'))
