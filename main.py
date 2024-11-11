from typing import Union, Optional, List
from db import Database
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserLogin(BaseModel):
    mail: str
    password: str


class User(BaseModel):
    fio: str
    address: str
    mail: str
    phone_number: str
    rating: float


class Rent(BaseModel):
    rent_id: int
    name: str
    price: str
    description: str
    user_id: int


class RentPage(BaseModel):
    Rents: List[Rent]


@app.get("/user")
def user_get(user: UserLogin):

    return {"Hello": "World"}


@app.post("/user")
def user_post(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/user")
def user_post(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/")
def main_page(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/rent")
def rent_get(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/rent")
def rent_get(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}