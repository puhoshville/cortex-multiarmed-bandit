import random

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Data(BaseModel):
    msg: str


@app.post("/")
def recommend(data: Data):
    """Returns random negative integers"""
    print(f"Model B. Input object {data}")
    return -random.randint(0, 100)
