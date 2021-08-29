from typing import Optional, List

from fastapi import FastAPI, Header

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: str, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def put_item(item_id: str, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/items/{item_id}")
def post_item(item_id: str, x_token: Optional[List[str]] = Header(None), item: Item = Item(name = "", price = 0.0)):
    return {"item_id": item_id, "x_token": x_token, "body": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: str, x_token: Optional[List[str]] = Header(None)):
    return {"item_id": item_id, "x_token": x_token}


