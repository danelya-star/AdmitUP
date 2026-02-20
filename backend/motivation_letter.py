from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from backend.claude_service import ClaudeService

router = APIRouter()

# Модель данных, которые мы ждем от фронтенда
class LetterRequest(BaseModel):
    university: str = Field(..., description="Название университета")
    program: str = Field(..., description="Название программы/специальности")
    background: str = Field(..., description="Бэкграунд студента: образование, опыт, достижения")
    goals: str = Field(..., description="Почему выбран этот вуз и какие карьерные цели")

# Инициализация сервиса
try:
    claude_service = ClaudeService()
except ValueError as e:
    claude_service = None
    print(f"Warning: ClaudeService not initialized in motivation_letter: {e}")


def create_letter_prompt(req: LetterRequest) -> str:
    """Создает промпт для генерации мотивационного письма."""
    return f"""
    Act as an expert academic admissions consultant. Write a professional, persuasive, and highly personalized Motivation Letter (Statement of Purpose) for a student applying to university.

    Target University: {req.university}
    Target Program: {req.program}

    Student's Background & Achievements:
    {req.background}

    Student's Goals & Reasons for Applying:
    {req.goals}

    Structure the letter formally: Introduction, Academic Background, Professional Experience (if any), Why this University/Program, and Conclusion.
    The tone should be academic, confident, and sincere.
    """

@router.post("/generate-letter/stream", tags=["Motivation Letter"])
async def generate_motivation_letter_stream(request: LetterRequest):
    """
    Генерирует мотивационное письмо с помощью Claude (стриминг).
    """
    if not claude_service:
        raise HTTPException(status_code=503, detail="AI Service is not configured properly.")

    prompt = create_letter_prompt(request)

    try:
        # Используем стриминг, так как письмо может быть длинным
        stream = claude_service.generate_response_stream(prompt, max_tokens=3000)
        return StreamingResponse(stream, media_type="text/plain")
    except Exception as e:
        print(f"Error generating letter: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate letter.")