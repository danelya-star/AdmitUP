import asyncio
import os
from motor.motor_asyncio import AsyncIOMotorClient

# Get connection details from environment variables or use defaults
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "mydatabase")

# Sample university data (you can expand this list)
universities_data = [
    {"name": "University of Cambridge", "country": "UK", "programs": ["Computer Science", "Law", "Medicine"]},
    {"name": "University of Oxford", "country": "UK", "programs": ["History", "Economics", "Physics"]},
    {"name": "Harvard University", "country": "USA", "programs": ["Business", "Political Science", "Biology"]},
    {"name": "Stanford University", "country": "USA", "programs": ["Engineering", "Arts", "Education"]},
    {"name": "Massachusetts Institute of Technology (MIT)", "country": "USA", "programs": ["Technology", "Science", "Architecture"]},
    {"name": "ETH Zurich", "country": "Switzerland", "programs": ["Engineering", "Natural Sciences"]},
    {"name": "National University of Singapore (NUS)", "country": "Singapore", "programs": ["Business", "Computing", "Dentistry"]},
    {"name": "University of Toronto", "country": "Canada", "programs": ["Medicine", "Law", "Engineering"]},
    {"name": "Tsinghua University", "country": "China", "programs": ["Engineering", "Computer Science"]},
    {"name": "The University of Tokyo", "country": "Japan", "programs": ["Science", "Law", "Economics"]},
    {"name": "University of Melbourne", "country": "Australia", "programs": ["Law", "Business", "Education"]},
    {"name": "University of Sydney", "country": "Australia", "programs": ["Medicine", "Arts", "Engineering"]},
    {"name": "McGill University", "country": "Canada", "programs": ["Medicine", "Law", "Music"]},
    {"name": "University of British Columbia", "country": "Canada", "programs": ["Forestry", "Business", "Science"]},
    {"name": "Imperial College London", "country": "UK", "programs": ["Science", "Engineering", "Medicine", "Business"]},
    {"name": "University College London (UCL)", "country": "UK", "programs": ["Education", "Architecture", "Psychology"]},
    {"name": "University of Edinburgh", "country": "UK", "programs": ["Informatics", "Humanities", "Medicine"]},
    {"name": "King's College London", "country": "UK", "programs": ["Law", "Health", "Humanities"]},
    {"name": "Princeton University", "country": "USA", "programs": ["Mathematics", "Physics", "Humanities"]},
    {"name": "Yale University", "country": "USA", "programs": ["Law", "Drama", "Art"]},
    {"name": "Columbia University", "country": "USA", "programs": ["Journalism", "Law", "Business"]},
    {"name": "University of Chicago", "country": "USA", "programs": ["Economics", "Sociology", "Law"]},
    {"name": "University of Pennsylvania", "country": "USA", "programs": ["Business (Wharton)", "Medicine", "Law"]},
    {"name": "California Institute of Technology (Caltech)", "country": "USA", "programs": ["Physics", "Chemistry", "Engineering"]},
    {"name": "EPFL", "country": "Switzerland", "programs": ["Engineering", "Technology", "Science"]},
    {"name": "University of Hong Kong", "country": "Hong Kong", "programs": ["Dentistry", "Education", "Linguistics"]},
    {"name": "Seoul National University", "country": "South Korea", "programs": ["Engineering", "Natural Sciences", "Business"]},
    {"name": "Peking University", "country": "China", "programs": ["Literature", "Science", "Management"]},
    {"name": "Sorbonne University", "country": "France", "programs": ["Humanities", "Science", "Medicine"]},
    {"name": "Technical University of Munich", "country": "Germany", "programs": ["Engineering", "Technology", "Physics"]},
]

async def seed_data():
    """Connects to MongoDB and seeds the universities collection."""
    client = AsyncIOMotorClient(MONGO_URL)
    db = client[MONGO_DB_NAME]
    collection = db["universities"]

    await collection.delete_many({})
    print("Cleared existing universities data.")

    result = await collection.insert_many(universities_data)
    print(f"Successfully inserted {len(result.inserted_ids)} universities.")

    client.close()

if __name__ == "__main__":
    print("Starting to seed university data...")
    asyncio.run(seed_data())
    print("Seeding complete.")