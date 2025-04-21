from pydantic import BaseModel
from typing import List

class ChatKeywordItem(BaseModel):
    keywords: List[str]
    answer: str