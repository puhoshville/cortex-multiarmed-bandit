import random

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Data(BaseModel):
    msg: str


@app.post("/")
def recommend(data: Data):
    """Returns random positive integers"""
    print(f"Model A. Input object {data}")
    return random.randint(0, 100)


@app.get("/ping")
def pong():
    return "OK"
