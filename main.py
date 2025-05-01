from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.chatbot import router as chatbot_router
# from dotenv import load_dotenv
# import os

app = FastAPI()

# react_host = os.getenv("REACT_APP_HOST", "http://localhost")
# react_port = os.getenv("REACT_APP_PORT", "3000")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://frontend-service:80"],  # React 앱이 동작하는 주소 (개발 중)
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)

app.include_router(chatbot_router)