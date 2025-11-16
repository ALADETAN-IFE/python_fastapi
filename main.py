from fastapi import FastAPI

app = FastAPI()

items = []

@app.get("/")
def read_root():
    return {"welcome" : "Hello World"}

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return {"message": item + " was added successfull", "data": items}


@app.get("/items")
def read_items():
    return items


@app.get("/items/{item_id}")
def read_item(item_id: int) -> str:
    item = items[item_id]
    return item


