from app.db import db
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_COLLECTION_NAME = os.getenv("MONGO_COLLECTION_NAME")

async def get_chatbot_response(question: str):
    collection = db[MONGO_COLLECTION_NAME]
    datas = collection.find()

    question_lower = question.lower()
    async for data in datas:
        # print(data)
        for keyword in data.get("keywords", []):
            if keyword.lower() in question_lower:
                return {"answer": data["answer"]}
    
    return {"answer": "죄송합니다. 아직 그 질문에 대한 답변은 준비되지 못했습니다. 다시 질문해주세요."}
