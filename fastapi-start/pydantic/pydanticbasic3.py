from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str = Field(..., title="Item Name", min_length=2, max_length=50)
    description: str = Field(None, description="The description of the item", max_length=3)
    price : float = Field(..., gte=0, description="The price must be greather than zero")
    tag: List[str] = Field(default=[], alias="item-tags")


@app.post("/items/")
async def create_item(item: Item):
    return {"item": item.dict()}

