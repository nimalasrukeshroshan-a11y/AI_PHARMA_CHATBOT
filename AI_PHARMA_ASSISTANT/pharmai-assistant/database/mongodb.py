"""
MongoDB connection setup and initialization.
Handles connection to MongoDB Atlas and database setup.
"""

import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB connection string from environment
MONGODB_URI = os.getenv("MONGODB_URI")

# Global database instance
db = None

def connect_to_mongodb():
    """
    Establish connection to MongoDB.
    Returns the database instance or None if connection fails.
    """
    global db
    try:
        client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
        # Test connection
        client.admin.command('ping')
        db = client.get_default_database()
        print("✅ Connected to MongoDB successfully")
        return db
    except (ConnectionFailure, ServerSelectionTimeoutError) as e:
        print(f"❌ Failed to connect to MongoDB: {e}")
        return None

def get_database():
    """
    Get the MongoDB database instance.
    If not connected, attempts to connect.
    """
    global db
    if db is None:
        db = connect_to_mongodb()
    return db

def init_collections():
    """
    Initialize MongoDB collections with proper structure.
    Creates indexes for better query performance.
    """
    try:
        database = get_database()
        if database is None:
            return False
        
        # Create users collection with unique email index
        if "users" not in database.list_collection_names():
            database.create_collection("users")
        database.users.create_index("email", unique=True)
        
        # Create query_history collection
        if "query_history" not in database.list_collection_names():
            database.create_collection("query_history")
        database.query_history.create_index("user_id")
        database.query_history.create_index("timestamp")
        
        print("✅ Collections initialized successfully")
        return True
    except Exception as e:
        print(f"❌ Error initializing collections: {e}")
        return False
