"""
Helper utilities for common operations.
Provides utility functions used across the application.
"""

from datetime import datetime

def format_timestamp(dt):
    """
    Format datetime object to readable string.
    
    Args:
        dt: Datetime object
    
    Returns:
        Formatted timestamp string
    """
    if isinstance(dt, datetime):
        return dt.strftime("%B %d, %Y at %I:%M %p")
    return str(dt)

def format_query_response(query, response):
    """
    Format query and response for display.
    
    Args:
        query: User's query
        response: AI response
    
    Returns:
        Formatted string with both query and response
    """
    return f"""
**Your Question:**
{query}

**AI Response:**
{response}
"""

def truncate_text(text, max_length=100):
    """
    Truncate text to maximum length with ellipsis.
    
    Args:
        text: Text to truncate
        max_length: Maximum length before truncation
    
    Returns:
        Truncated text with ellipsis if longer than max_length
    """
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text

def convert_to_list(input_value):
    """
    Convert various input formats to list.
    Handles strings, lists, and comma-separated values.
    
    Args:
        input_value: Input in various formats
    
    Returns:
        List of items
    """
    if isinstance(input_value, list):
        return input_value
    
    if isinstance(input_value, str):
        return [item.strip() for item in input_value.split(",") if item.strip()]
    
    return []

def get_user_display_name(user):
    """
    Get display name from user object.
    
    Args:
        user: User object from database
    
    Returns:
        User's display name
    """
    if not user:
        return "Guest"
    
    name = user.get('name', 'User')
    return name.split()[0] if name else "User"  # Return first name

def is_empty_or_whitespace(value):
    """
    Check if value is empty or contains only whitespace.
    
    Args:
        value: Value to check
    
    Returns:
        True if empty or whitespace, False otherwise
    """
    if isinstance(value, str):
        return not value or not value.strip()
    return not value

def safe_get_dict_value(dictionary, key, default=None):
    """
    Safely get value from dictionary with default.
    
    Args:
        dictionary: Dictionary to access
        key: Key to retrieve
        default: Default value if key not found
    
    Returns:
        Value from dictionary or default
    """
    try:
        return dictionary.get(key, default)
    except AttributeError:
        return default
