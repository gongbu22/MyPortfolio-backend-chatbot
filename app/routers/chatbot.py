from fastapi import APIRouter, Query
from pydantic import BaseModel
from app.service.chatbot import get_chatbot_response

router = APIRouter()


@router.post("/chatbot")
async def chatbot_res(req: ChatRequest):
    return await get_chatbot_response(req.question)
