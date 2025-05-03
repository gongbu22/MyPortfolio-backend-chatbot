from app.models.aboutme import aboutme

async def get_chatbot_response(question: str) -> dict:
    question_lower = question.lower()
    async for data in aboutme.find_all():
        # print(data)
        for keyword in data.keywords:
            if keyword.lower() in question_lower:
                return {"answer": data.answer}
    
    return {"answer": "죄송합니다. 아직 그 질문에 대한 답변은 준비되지 못했습니다. 다시 질문해주세요."}
