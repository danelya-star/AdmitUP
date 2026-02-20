from pydantic import BaseModel, field_validator
from typing import List

class University(BaseModel):
    name: str
    country: str
    programs: List[str] = []

    @field_validator('name', 'country')
    @classmethod
    def not_empty(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError('Field cannot be empty or whitespace only')
        return v
