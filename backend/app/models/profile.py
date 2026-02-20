from pydantic import BaseModel
from typing import Optional

class OnboardingData(BaseModel):
    level: Optional[str] = None
    status: Optional[str] = None
    country: Optional[str] = None
    major: Optional[str] = None # направление
    language: Optional[str] = None
    goal: Optional[str] = None