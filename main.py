from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Characteristics(BaseModel):
    ram_memory: float
    rom_memory: float


class Phone(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristics

phones = []

@app.get("/health")
async def health():
    return "OK"

@app.post("/phones", status_code=201)
async def create_phone(phone: Phone):
    phones.append(phone.dict())
    return {"message": "Phone created"}

@app.get("/phones")
async def get_phones():
    return phones

@app.get("/phones/{id}")
async def get_phone(id: str):
    for phone in phones:
        if phone["identifier"] == id:
            return phone
    raise HTTPException(status_code=404, detail="Phone with provided id does not exist or was not found")
