from fastapi import APIRouter, Depends, HTTPException
from typing import List, Dict, Any
from motor.motor_asyncio import AsyncIOMotorDatabase
from ..db import get_database
from ..models.plan import Plan, PlanCreate
from bson import ObjectId
from pymongo.errors import PyMongoError
from .auth import get_current_user
import os
import json
from openai import AsyncOpenAI

router = APIRouter()

@router.post("/", status_code=201)
async def create_plan(
    plan_data: PlanCreate, 
    db: AsyncIOMotorDatabase = Depends(get_database),
    current_user: dict = Depends(get_current_user)
):
    plan = Plan(
        user_id=str(current_user["_id"]),
        plan=plan_data.plan
    )

    try:
        result = await db["plans"].insert_one(plan.dict())
        return {"plan_id": str(result.inserted_id)}
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@router.post("/generate", status_code=201)
async def generate_plan(
    db: AsyncIOMotorDatabase = Depends(get_database),
    current_user: dict = Depends(get_current_user)
):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="OpenAI API key not configured")

    profile = current_user.get("onboarding_profile")
    if not profile:
        raise HTTPException(status_code=400, detail="Profile not found. Please complete onboarding first.")

    client = AsyncOpenAI(api_key=api_key)

    prompt = f"""
    Act as an experienced IELTS tutor. Create a personalized study plan for a student with the following profile:
    - Current Level: {profile.get('level', 'Intermediate')}
    - Target Goal: {profile.get('goal', 'Band 7.0')}
    - Status: {profile.get('status', 'Student')}
    - Major/Interest: {profile.get('major', 'General')}
    - Target Country: {profile.get('country', 'UK')}
    - Native Language: {profile.get('language', 'Russian')}

    The plan should be for 1 week (as a sample MVP).
    Provide the response in strict JSON format with the following structure:
    {{
        "title": "Personalized IELTS Study Plan",
        "overview": "Brief strategy description",
        "schedule": [
            {{
                "day": "Monday",
                "focus": "Listening & Vocabulary",
                "tasks": ["Task 1 description...", "Task 2 description..."]
            }},
            ... (continue for 7 days)
        ]
    }}
    """

    try:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo-1106", # Используем модель с поддержкой JSON mode
            messages=[
                {"role": "system", "content": "You are a helpful assistant that outputs JSON."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )
        
        content = response.choices[0].message.content
        generated_plan_data = json.loads(content)
        
        # Создаем объект плана
        plan_model = Plan(
            user_id=str(current_user["_id"]),
            plan=generated_plan_data
        )
        
        # Сохраняем в БД
        result = await db["plans"].insert_one(plan_model.dict())
        
        return {
            "plan_id": str(result.inserted_id),
            "plan": generated_plan_data
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Generation failed: {str(e)}")

@router.get("/", response_model=List[Dict[str, Any]])
async def get_my_plans(
    db: AsyncIOMotorDatabase = Depends(get_database),
    current_user: dict = Depends(get_current_user)
):
    try:
        cursor = db["plans"].find({"user_id": str(current_user["_id"])})
        plans = await cursor.to_list(length=100)
        for plan in plans:
            plan["id"] = str(plan["_id"])
            del plan["_id"]
        return plans
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@router.get("/{plan_id}")
async def get_plan(plan_id: str, db: AsyncIOMotorDatabase = Depends(get_database)):
    if not ObjectId.is_valid(plan_id):
        raise HTTPException(status_code=400, detail="Invalid plan_id")
    
    try:
        plan = await db["plans"].find_one({"_id": ObjectId(plan_id)})
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    return {"plan": plan.get("plan")}
