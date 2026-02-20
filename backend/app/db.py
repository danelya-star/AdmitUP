from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "mydatabase")

class DataBase:
    client: AsyncIOMotorClient = None
    db: AsyncIOMotorDatabase = None

db = DataBase()

async def get_database() -> AsyncIOMotorDatabase:
    """Dependency function to get the database instance."""
    return db.db

async def connect_to_mongo():
    """Connects to MongoDB and initializes the database."""
    db.client = AsyncIOMotorClient(MONGO_URL)
    db.db = db.client[MONGO_DB_NAME]

async def close_mongo_connection():
    """Closes the MongoDB connection."""
    db.client.close()
