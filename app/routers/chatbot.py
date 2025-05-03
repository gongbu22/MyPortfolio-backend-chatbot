from fastapi import APIRouter
from app.schema.chatbot import ChatRequest, ChatResponse
from app.service.chatbot import get_chatbot_response

router = APIRouter()

@router.post("/chatbot", response_model=ChatResponse)
async def chatbot_res(req: ChatRequest):
    return await get_chatbot_response(req.question)
