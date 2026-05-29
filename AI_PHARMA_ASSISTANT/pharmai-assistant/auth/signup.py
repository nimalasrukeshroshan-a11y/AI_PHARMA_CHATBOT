"""
Signup logic for new user registration.
Handles user registration and input validation.
"""

from auth.security import hash_password
from database.queries import create_user, email_exists

def register_user(name, email, password, age, allergies_str, conditions_str, medications_str):
    """
    Register a new user in the system.
    
    Args:
        name: User's full name
        email: User's email address
        password: User's password (plain text)
        age: User's age
        allergies_str: Comma-separated allergies string
        conditions_str: Comma-separated conditions string
        medications_str: Comma-separated medications string
    
    Returns:
        User object if registration successful, None otherwise
    """
    try:
        # Validate inputs
        is_valid, error_msg = validate_signup_inputs(name, email, password, age, allergies_str, conditions_str, medications_str)
        if not is_valid:
            print(f"❌ Validation error: {error_msg}")
            return None, error_msg
        
        # Check if email already exists
        if email_exists(email):
            print(f"❌ Email already registered: {email}")
            return None, "Email already registered. Please use a different email or login."
        
        # Convert comma-separated strings to lists
        allergies = [a.strip() for a in allergies_str.split(",") if a.strip()]
        conditions = [c.strip() for c in conditions_str.split(",") if c.strip()]
        medications = [m.strip() for m in medications_str.split(",") if m.strip()]
        
        # Hash password
        hashed_password = hash_password(password)
        
        # Create user in database
        success = create_user(name, email, hashed_password, age, allergies, conditions, medications)
        
        if success:
            print(f"✅ User {email} registered successfully")
            # Return user object for automatic login
            return {
                "name": name,
                "email": email,
                "age": age,
                "known_allergies": allergies,
                "existing_conditions": conditions,
                "current_medications": medications
            }, ""
        else:
            return None, "Failed to register user. Please try again."
    except Exception as e:
        print(f"❌ Registration error: {e}")
        return None, f"Registration error: {str(e)}"

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

def validate_signup_inputs(name, email, password, age, allergies, conditions, medications):
    """
    Validate signup form inputs.
    
    Args:
        name: User's name
        email: User's email
        password: User's password
        age: User's age
        allergies: Allergies string
        conditions: Conditions string
        medications: Medications string
    
    Returns:
        Tuple (is_valid, error_message)
    """
    if not name or not name.strip():
        return False, "Name is required"
    
    if len(name.strip()) < 2:
        return False, "Name must be at least 2 characters"
    
    if not email or not email.strip():
        return False, "Email is required"
    
    if not is_valid_email(email):
        return False, "Invalid email format"
    
    if not password or not password.strip():
        return False, "Password is required"
    
    if len(password) < 6:
        return False, "Password must be at least 6 characters"
    
    try:
        age_int = int(age)
        if age_int < 1 or age_int > 150:
            return False, "Age must be between 1 and 150"
    except ValueError:
        return False, "Age must be a valid number"
    
    return True, ""
