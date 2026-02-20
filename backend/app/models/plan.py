from pydantic import BaseModel, field_validator
from typing import Dict, Any

class PlanCreate(BaseModel):
    plan: Dict[str, Any]

    @field_validator('plan')
    @classmethod
    def plan_not_empty(cls, v: Dict[str, Any]) -> Dict[str, Any]:
        if not v:
            raise ValueError('Plan data cannot be empty')
        return v

class Plan(PlanCreate):
    user_id: str
