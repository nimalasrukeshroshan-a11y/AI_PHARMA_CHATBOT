"""
Input validation utilities.
Validates user inputs across the application.
"""

def validate_email(email):
    """
    Validate email format.
    
    Args:
        email: Email address to validate
    
    Returns:
        Tuple (is_valid, error_message)
    """
    import re
    
    if not email or not email.strip():
        return False, "Email is required"
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        return False, "Invalid email format"
    
    return True, ""

def validate_password(password):
    """
    Validate password strength.
    
    Args:
        password: Password to validate
    
    Returns:
        Tuple (is_valid, error_message)
    """
    if not password or not password.strip():
        return False, "Password is required"
    
    if len(password) < 6:
        return False, "Password must be at least 6 characters"
    
    return True, ""

def validate_name(name):
    """
    Validate user name.
    
    Args:
        name: Name to validate
    
    Returns:
        Tuple (is_valid, error_message)
    """
    if not name or not name.strip():
        return False, "Name is required"
    
    if len(name.strip()) < 2:
        return False, "Name must be at least 2 characters"
    
    return True, ""

def validate_age(age):
    """
    Validate user age.
    
    Args:
        age: Age to validate (as int or string)
    
    Returns:
        Tuple (is_valid, error_message)
    """
    try:
        age_int = int(age)
        if age_int < 1 or age_int > 150:
            return False, "Age must be between 1 and 150"
        return True, ""
    except ValueError:
        return False, "Age must be a valid number"

def parse_comma_separated(text):
    """
    Parse comma-separated string into list.
    Handles empty strings and whitespace.
    
    Args:
        text: Comma-separated string
    
    Returns:
        List of items with whitespace stripped
    """
    if not text or not text.strip():
        return []
    
    return [item.strip() for item in text.split(",") if item.strip()]

def sanitize_input(user_input):
    """
    Sanitize user input to prevent injection attacks.
    
    Args:
        user_input: User input string
    
    Returns:
        Sanitized string
    """
    if not isinstance(user_input, str):
        return user_input
    
    # Remove leading/trailing whitespace
    sanitized = user_input.strip()
    
    # Limit input length to prevent abuse
    if len(sanitized) > 5000:
        sanitized = sanitized[:5000]
    
    return sanitized
