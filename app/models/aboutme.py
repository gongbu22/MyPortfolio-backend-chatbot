from typing import List
from beanie import Document
from bson import ObjectId

class aboutme(Document):
    # _id: ObjectId
    keywords: List[str]
    answer: str

    class Settings:
        collection = "aboutme"