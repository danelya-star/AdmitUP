import os
import anthropic
from dotenv import load_dotenv
from typing import AsyncGenerator

# Загрузка переменных окружения
load_dotenv()

class ClaudeService:
    def __init__(self):
        # Получаем ключ из переменных окружения
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY не найден. Проверьте файл .env")
        
        # Инициализация клиента Anthropic
        # Используем асинхронный клиент для совместимости с FastAPI
        self.client = anthropic.AsyncAnthropic(
            api_key=self.api_key,
        )

    async def generate_response(self, prompt: str, model: str = "claude-3-sonnet-20240229", max_tokens: int = 1024) -> str:
        """
        Отправляет запрос к Claude и возвращает текстовый ответ.
        """
        try:
            message = await self.client.messages.create(
                model=model,
                max_tokens=max_tokens,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ]
            )
            return message.content[0].text
        except Exception as e:
            print(f"Ошибка при запросе к Claude: {e}")
            raise e

    async def generate_response_stream(self, prompt: str, model: str = "claude-3-sonnet-20240229", max_tokens: int = 2048) -> AsyncGenerator[str, None]:
        """
        Отправляет запрос к Claude и возвращает ответ в виде асинхронного потока (стриминг).
        """
        try:
            # Используем асинхронный контекстный менеджер для стриминга
            async with self.client.messages.stream(
                model=model,
                max_tokens=max_tokens,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ]
            ) as stream:
                # Асинхронно итерируемся по частям текста
                async for text in stream.text_stream:
                    yield text
        except Exception as e:
            print(f"Ошибка при стриминге ответа от Claude: {e}")
            raise e