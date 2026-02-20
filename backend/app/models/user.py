from pydantic import BaseModel, field_validator, EmailStr
from typing import Optional
from .profile import OnboardingData

class User(BaseModel):
    name: str
    email: EmailStr
    role: str
    onboarding_profile: Optional[OnboardingData] = None

    @field_validator('name')
    @classmethod
    def name_must_be_valid(cls, v: str) -> str:
        if len(v) < 2:
            raise ValueError('Name must be at least 2 characters long')
        return v

    @field_validator('role')
    @classmethod
    def role_must_be_valid(cls, v: str) -> str:
        allowed_roles = {'student', 'teacher', 'admin', 'user'}
        if v not in allowed_roles:
            raise ValueError(f'Role must be one of: {", ".join(allowed_roles)}')
        return v

class UserCreate(User):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str