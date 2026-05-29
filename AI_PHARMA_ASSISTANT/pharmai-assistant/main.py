"""
Main backend controller for PharmAI Assistant.
Handles business logic and orchestrates between UI and services.
"""

import streamlit as st
from datetime import datetime
from auth.login import login_user, validate_login_inputs
from auth.signup import register_user, validate_signup_inputs
from ai.ollama_client import generate_response
from ai.prompt_builder import build_general_medication_prompt
from database.queries import save_query_history, get_user_query_history, get_user_by_id
from utils.validators import sanitize_input
from bson import ObjectId

def handle_login(email, password):
    """
    Handle user login logic.
    
    Args:
        email: User's email
        password: User's password
    
    Returns:
        Tuple (success, user_object, error_message)
    """
    # Validate inputs
    is_valid, error_msg = validate_login_inputs(email, password)
    if not is_valid:
        return False, None, error_msg
    
    # Attempt login
    user = login_user(email, password)
    if user:
        # Convert ObjectId to string for storage
        user['_id'] = str(user.get('_id', ''))
        return True, user, ""
    else:
        return False, None, "Invalid email or password"

def handle_signup(name, email, password, age, allergies, conditions, medications):
    """
    Handle user registration logic.
    
    Args:
        name: User's name
        email: User's email
        password: User's password
        age: User's age
        allergies: Allergies string
        conditions: Conditions string
        medications: Medications string
    
    Returns:
        Tuple (success, user_object, error_message)
    """
    user, error_msg = register_user(name, email, password, age, allergies, conditions, medications)
    return (user is not None), user, error_msg

def handle_medication_query(user, query_text):
    """
    Handle medication query and generate AI response.
    
    Args:
        user: Current user object
        query_text: User's query about medication
    
    Returns:
        Tuple (success, response_text, error_message)
    """
    try:
        # Sanitize input
        sanitized_query = sanitize_input(query_text)
        
        if not sanitized_query:
            return False, "", "Please enter a valid question"
        
        # Build personalized prompt
        prompt = build_general_medication_prompt(sanitized_query, user)
        
        # Generate AI response
        response = generate_response(prompt, user)
        
        if response and not response.startswith("Error"):
            # Save to query history
            user_id = user.get('_id')
            if user_id:
                save_query_history(user_id, sanitized_query, response)
            
            return True, response, ""
        else:
            return False, "", response or "Failed to generate response"
    except Exception as e:
        print(f"❌ Error handling medication query: {e}")
        return False, "", f"Error processing your query: {str(e)}"

def get_user_history(user):
    """
    Retrieve user's query history.
    
    Args:
        user: Current user object
    
    Returns:
        List of query history items
    """
    try:
        user_id = user.get('_id')
        if user_id:
            return get_user_query_history(user_id, limit=10)
        return []
    except Exception as e:
        print(f"❌ Error retrieving query history: {e}")
        return []

def refresh_user_profile(user):
    """
    Refresh user profile from database.
    
    Args:
        user: User object with _id field
    
    Returns:
        Updated user object or None if not found
    """
    try:
        user_id = user.get('_id')
        if user_id:
            updated_user = get_user_by_id(user_id)
            if updated_user:
                updated_user['_id'] = str(updated_user.get('_id', ''))
                return updated_user
        return user
    except Exception as e:
        print(f"❌ Error refreshing user profile: {e}")
        return user
