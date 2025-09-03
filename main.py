from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def root():
    return {"message:" "Ok"}

@app.post("/phone")
async def create_phone(phone: dict):
    return {"message": "Phone created", "phone": phone}

@app.get("/phone")
async def get_phones():
    return {"message": "List of phones", "phones": []}

@app.get("/phone/{phone_id}")
async def get_phone(phone_id: int):
    return {"message": "Phone details", "phone": {"id": phone_id, "brand": "Example", "model": "Example"}}

@app.put("/phone/{phone_id}")
async def update_phone(phone_id: int, phone: dict):
    return {"message": "Phone updated", "phone": {"id": phone_id, **phone}}
