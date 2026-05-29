"""
Security utilities for password hashing and verification.
Uses bcrypt for secure password handling.
"""

import bcrypt

def hash_password(password):
    """
    Hash a password using bcrypt.
    
    Args:
        password: Plain text password to hash
    
    Returns:
        Hashed password string
    """
    # Generate salt and hash the password
    salt = bcrypt.gensalt(rounds=12)
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(password, hashed_password):
    """
    Verify a password against a bcrypt hash.
    
    Args:
        password: Plain text password to verify
        hashed_password: Bcrypt hash to compare against
    
    Returns:
        True if password matches, False otherwise
    """
    try:
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
    except Exception as e:
        print(f"❌ Error verifying password: {e}")
        return False
