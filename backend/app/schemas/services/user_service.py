from app.database import db

def create_user(user_data: dict):
    collection = db.users
    result = collection.insert_one(user_data)
    return str(result.inserted_id)

def get_all_users():
    collection = db.users
    users = list(collection.find({}, {"_id": 0}))
    return users
