"""
Login logic for user authentication.
Handles user login verification and session management.
"""

from auth.security import verify_password
from database.queries import get_user_by_email

def login_user(email, password):
    """
    Authenticate user with email and password.
    
    Args:
        email: User's email address
        password: User's plain text password
    
    Returns:
        User object if login successful, None otherwise
    """
    try:
        # Retrieve user from database
        user = get_user_by_email(email)
        
        if user is None:
            print("❌ User not found")
            return None
        
        # Verify password
        if verify_password(password, user["password"]):
            print(f"✅ User {email} logged in successfully")
            return user
        else:
            print("❌ Invalid password")
            return None
    except Exception as e:
        print(f"❌ Login error: {e}")
        return None

def is_valid_email(email):
    """
    Validate email format.
    
    Args:
        email: Email address to validate
    
    Returns:
        True if email format is valid, False otherwise
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_login_inputs(email, password):
    """
    Validate login form inputs.
    
    Args:
        email: User's email
        password: User's password
    
    Returns:
        Tuple (is_valid, error_message)
    """
    if not email or not email.strip():
        return False, "Email is required"
    
    if not password or not password.strip():
        return False, "Password is required"
    
    if not is_valid_email(email):
        return False, "Invalid email format"
    
    if len(password) < 6:
        return False, "Password must be at least 6 characters"
    
    return True, ""
