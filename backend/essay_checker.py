from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel, Field
from backend.claude_service import ClaudeService

# Модель для входящего запроса, чтобы FastAPI знал, какие данные ожидать
class EssayRequest(BaseModel):
    text: str = Field(..., min_length=50, description="Текст эссе для проверки")
    topic: str = Field(..., min_length=10, description="Тема, на которую написано эссе")

router = APIRouter()

# Мы создаем один экземпляр сервиса, чтобы не делать это при каждом запросе.
# Это более эффективно.
try:
    claude_service = ClaudeService()
except ValueError as e:
    # Если ключ API не найден, сервис не будет работать.
    claude_service = None
    print(f"КРИТИЧЕСКАЯ ОШИБКА: Не удалось инициализировать ClaudeService: {e}")


@router.post("/check-essay", tags=["IELTS Checker"])
async def check_ielts_essay(request: EssayRequest):
    """
    Принимает текст эссе и его тему, отправляет на проверку в Claude
    и возвращает результат.
    """
    if not claude_service:
        raise HTTPException(
            status_code=503, # Service Unavailable
            detail="Сервис проверки эссе временно недоступен из-за ошибки конфигурации."
        )

    # Формируем более качественный и структурированный промпт для Claude
    prompt = f"""
    Please act as an experienced IELTS examiner. Analyze the following essay written on the topic: "{request.topic}".

    Provide a detailed analysis based on the four official IELTS writing criteria: Task Achievement, Cohesion and Coherence, Lexical Resource, and Grammatical Range and Accuracy.

    For each criterion, provide an estimated band score and specific reasons for that score.
    Conclude with an overall estimated band score and actionable suggestions for improvement.

    Essay to analyze:
    ---
    {request.text}
    ---
    """

    try:
        feedback = claude_service.generate_response(prompt, max_tokens=2048)
        return {"feedback": feedback}
    except Exception as e:
        print(f"Произошла ошибка при обращении к API Claude: {e}")
        raise HTTPException(
            status_code=500,
            detail="Не удалось получить ответ от сервиса проверки."
        )