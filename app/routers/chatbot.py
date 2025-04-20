from fastapi import APIRouter, Query
from app.services.chatbot import get_chatbot_response

router = APIRouter()

@router.get("/chatbot")
async def chatbot_res(que: str = Query(..., description='질문을 입력하세요.')):
    return await get_chatbot_response(que)
