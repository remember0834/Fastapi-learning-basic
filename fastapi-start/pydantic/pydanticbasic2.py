from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):  # Pydantic 모델 정의
    name : str
    description : Optional[str] = None # 선택적 필드
    price: float
    tax : float = 0.1

@app.post("/items/")
async def create_item(item: Item):
    return {"item": item.dict()}