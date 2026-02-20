from fastapi import APIRouter, HTTPException, Depends
from ..models import User
from ..models.profile import OnboardingData
from .. import crud
from typing import List, Dict, Any
from ..exceptions import UserAlreadyExistsException, DatabaseConnectionException
from .auth import get_current_user
from ..db import get_database
from motor.motor_asyncio import AsyncIOMotorDatabase
from bson import ObjectId
from pymongo.errors import PyMongoError

router = APIRouter()

@router.get("/", response_model=List[Dict[str, Any]])
async def get_users():
    try:
        return await crud.list_users()
    except DatabaseConnectionException as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/", status_code=201)
async def create_new_user(user: User):
    try:
        user_id = await crud.create_user(user)
        return {"message": "Пользователь создан", "user_id": user_id}
    except UserAlreadyExistsException as e:
        raise HTTPException(status_code=400, detail=str(e))
    except DatabaseConnectionException as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/me/onboarding", status_code=200)
async def save_onboarding_data(
    onboarding_data: OnboardingData,
    db: AsyncIOMotorDatabase = Depends(get_database),
    current_user: dict = Depends(get_current_user)
):
    try:
        result = await db["users"].update_one(
            {"_id": ObjectId(current_user["_id"])},
            {"$set": {"onboarding_profile": onboarding_data.dict()}}
        )
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="User not found")
        
        return {"message": "Onboarding data saved successfully"}
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
