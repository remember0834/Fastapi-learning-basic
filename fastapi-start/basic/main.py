from fastapi import FastAPI

app = FastAPI()

@app.get("/itmes/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/getdata/")
def read_items(data: str = "funcoding"):
    return {"data": data}

# uvicorn main:app --reload 실행 

