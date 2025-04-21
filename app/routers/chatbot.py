from fastapi import APIRouter, Query
from pydantic import BaseModel
from app.services.chatbot import get_chatbot_response

router = APIRouter()

class ChatRequest(BaseModel):
    question: str

@router.post("/chatbot")
async def chatbot_res(req: ChatRequest):
    return await get_chatbot_response(req.question)
