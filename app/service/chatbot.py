from app.models.aboutme import aboutme
from app.schema.chatbot import ChatResponse

async def get_chatbot_response(question: str) -> ChatResponse:
    question_lower = question.lower()
    async for data in aboutme.find_all():
        # print(data)
        for keyword in data.keywords:
            if keyword.lower() in question_lower:
                return ChatResponse(answer=data.answer)
    
    return ChatResponse(answer="죄송합니다. 아직 그 질문에 대한 답변은 준비되지 못했습니다. 다시 질문해주세요.")
