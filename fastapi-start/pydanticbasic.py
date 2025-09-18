#from fastapi import FastAPI
#from pydantic import BaseModel
#
#app = FastAPI()
#
#class Item(BaseModel): #Pydnantic 모델 정의 
#    name : str
#    price : float
#    is_offer : bool = None # 기본값을 None으로 설정
#
#
#@app.post("/item/")
#def create_item(item: Item):
#    return {"item" : item.dict()} # Pydantic 모델을 API에 사용 
#


#from fastapi import FastAPI
#from pydantic import BaseModel
#from typing import Optional
#
#app = FastAPI()
#
#class Item(BaseModel):  # Pydantic 모델 정의
#    name : str
#    description : Optional[str] = None # 선택적 필드
#    price: float
#    tax : float = 0.1
#
#@app.post("/items/")
#async def create_item(item: Item):
#    return {"item": item.dict()}


#from fastapi import FastAPI
#from pydantic import BaseModel, Field
#from typing import List
#
#app = FastAPI()
#
#class Item(BaseModel):
#    name : str = Field(..., title= "Item Name", min_length=2, max_length=50)
#    description : str = Field(None, description= "The description of the item", max_length=300)
#    price: float = Field(..., gt=0, description= "The price must be greater than zero")
#    tag: List[str] = Field(default=[], alias="item-tags")
#
#@app.post("/items/")
#async def create_item(item: Item):
#    return {"item": item.dict()}


#from fastapi import FastAPI
#from pydantic import BaseModel
#
#app = FastAPI()
#
#class Image(BaseModel):
#    url: str
#    name: str
#
#class Item(BaseModel):
#    name: str
#    description: str
#    image: Image
#
#@app.post("/items/")
#def create_item(item: Item):
#    return {"item": item.dict()}

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Union

app= FastAPI()

class Item(BaseModel):
    name: str
    tags: List[str]
    variant: Union[int, str] # int 또는 str 타입을 허용하는 필드

@app.post("/items/")
def create_item(item: Item):
    return {"item": item.dict()}


