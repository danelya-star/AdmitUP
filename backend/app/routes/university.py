from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase
from ..db import get_database
from ..models.university import University
from pymongo.errors import PyMongoError
from typing import Optional

router = APIRouter()

@router.get("/")
async def get_universities(
    name: Optional[str] = None,
    country: Optional[str] = None,
    program: Optional[str] = None,
    db: AsyncIOMotorDatabase = Depends(get_database)
):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if country:
        query["country"] = {"$regex": country, "$options": "i"}
    if program:
        query["programs"] = {"$regex": program, "$options": "i"}

    try:
        unis_cursor = db["universities"].find(query, {"_id": 0})
        unis = await unis_cursor.to_list(length=100)
        return {"universities": unis}
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@router.post("/")
async def create_university(university: University, db: AsyncIOMotorDatabase = Depends(get_database)):
    try:
        await db["universities"].insert_one(university.dict())
        return {"message": "Университет добавлен", "university": university}
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
