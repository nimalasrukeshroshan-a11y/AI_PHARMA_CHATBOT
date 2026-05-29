"""
Database operations for users and query history.
Handles all MongoDB CRUD operations with proper error handling.
"""

from datetime import datetime
from bson import ObjectId
from pymongo.errors import DuplicateKeyError, PyMongoError
from database.mongodb import get_database

def create_user(name, email, hashed_password, age, allergies, conditions, medications):
    """
    Create a new user in the database.
    
    Args:
        name: User's full name
        email: User's email (unique)
        hashed_password: Bcrypt hashed password
        age: User's age
        allergies: List of known allergies
        conditions: List of existing health conditions
        medications: List of current medications
    
    Returns:
        True if user created successfully, False otherwise
    """
    try:
        database = get_database()
        if database is None:
            return False
        
        user_data = {
            "name": name,
            "email": email,
            "password": hashed_password,
            "age": age,
            "known_allergies": allergies if isinstance(allergies, list) else [],
            "existing_conditions": conditions if isinstance(conditions, list) else [],
            "current_medications": medications if isinstance(medications, list) else [],
            "created_at": datetime.now()
        }
        
        result = database.users.insert_one(user_data)
        return result.inserted_id is not None
    except DuplicateKeyError:
        print("❌ Email already exists")
        return False
    except PyMongoError as e:
        print(f"❌ Database error creating user: {e}")
        return False

def get_user_by_email(email):
    """
    Retrieve user from database by email.
    
    Args:
        email: User's email address
    
    Returns:
        User dictionary or None if not found
    """
    try:
        database = get_database()
        if database is None:
            return None
        
        user = database.users.find_one({"email": email})
        return user
    except PyMongoError as e:
        print(f"❌ Database error retrieving user: {e}")
        return None

def get_user_by_id(user_id):
    """
    Retrieve user from database by user ID.
    
    Args:
        user_id: ObjectId of the user
    
    Returns:
        User dictionary or None if not found
    """
    try:
        database = get_database()
        if database is None:
            return None
        
        user = database.users.find_one({"_id": ObjectId(user_id)})
        return user
    except PyMongoError as e:
        print(f"❌ Database error retrieving user by ID: {e}")
        return None

def save_query_history(user_id, query, response):
    """
    Save user's query and AI response to history.
    
    Args:
        user_id: ObjectId of the user
        query: User's question/query
        response: AI-generated response
    
    Returns:
        True if saved successfully, False otherwise
    """
    try:
        database = get_database()
        if database is None:
            return False
        
        history_data = {
            "user_id": ObjectId(user_id),
            "query": query,
            "response": response,
            "timestamp": datetime.now()
        }
        
        result = database.query_history.insert_one(history_data)
        return result.inserted_id is not None
    except PyMongoError as e:
        print(f"❌ Database error saving query history: {e}")
        return False

def get_user_query_history(user_id, limit=10):
    """
    Retrieve user's query history from database.
    
    Args:
        user_id: ObjectId of the user
        limit: Maximum number of queries to retrieve (default: 10)
    
    Returns:
        List of query history documents sorted by latest first
    """
    try:
        database = get_database()
        if database is None:
            return []
        
        history = list(
            database.query_history.find(
                {"user_id": ObjectId(user_id)}
            ).sort("timestamp", -1).limit(limit)
        )
        return history
    except PyMongoError as e:
        print(f"❌ Database error retrieving query history: {e}")
        return []

def email_exists(email):
    """
    Check if email already exists in database.
    
    Args:
        email: Email address to check
    
    Returns:
        True if email exists, False otherwise
    """
    try:
        database = get_database()
        if database is None:
            return False
        
        user = database.users.find_one({"email": email})
        return user is not None
    except PyMongoError as e:
        print(f"❌ Database error checking email: {e}")
        return False
