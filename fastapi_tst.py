from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel
import math

app = FastAPI()

class NumberInput(BaseModel):
    number: str

class SqrtResult(BaseModel):
    number: float
    sqrt: float

history = []

@app.post("/api/v1/sqrt", response_model=SqrtResult)
async def calculate_sqrt(number_input: NumberInput):
    number_str = number_input.number

    # If there's no dot but a comma is present, replace comma with dot
    if "." not in number_str and "," in number_str:
        number_str = number_str.replace(",", ".")

    try:
        number = float(number_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid number format.")

    # Check for negative numbers
    if number < 0:
        raise HTTPException(status_code=400, detail="Number must be non-negative.")

    sqrt = math.sqrt(number)
    result = {"number": number, "sqrt": sqrt}
    history.append(result)
    if len(history) > 4:
        history.pop(0)
    return result

@app.get("/api/v1/sqrt", response_model=List[SqrtResult])
async def get_sqrt():
    return history

