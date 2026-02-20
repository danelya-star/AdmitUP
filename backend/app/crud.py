from .models import User
from .db import db as database_wrapper
from typing import List, Dict, Any
from .exceptions import UserAlreadyExistsException, DatabaseConnectionException
from pymongo.errors import PyMongoError

async def create_user(user: User) -> str:
    db = database_wrapper.db
    if db is None:
        raise DatabaseConnectionException("Database not initialized")

    try:
        existing_user = await db["users"].find_one({"name": user.name})
        if existing_user:
            raise UserAlreadyExistsException(user.name)

        result = await db["users"].insert_one(user.dict())
        return str(result.inserted_id)
    except PyMongoError as e:
        raise DatabaseConnectionException(str(e))

async def get_user(name: str) -> Dict[str, Any] | None:
    db = database_wrapper.db
    if db is None:
        raise DatabaseConnectionException("Database not initialized")
    try:
        user = await db["users"].find_one({"name": name})
        if user:
            user["_id"] = str(user["_id"])
        return user
    except PyMongoError as e:
        raise DatabaseConnectionException(str(e))

async def list_users() -> List[Dict[str, Any]]:
    db = database_wrapper.db
    if db is None:
        raise DatabaseConnectionException("Database not initialized")
    users = []
    try:
        cursor = db["users"].find()
        async for user_doc in cursor:
            user_doc["_id"] = str(user_doc["_id"])
            users.append(user_doc)
        return users
    except PyMongoError as e:
        raise DatabaseConnectionException(str(e))
