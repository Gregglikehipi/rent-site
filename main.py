import uuid
from typing import Union, Optional, List, Annotated

from sqlalchemy.orm import Session

from logic import check_token

from db import Database
from fastapi import FastAPI, Request, Depends, status, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

from pydantic import BaseModel
from model import db_helper
from crud import *

app = FastAPI()

'''
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
'''

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="static/templates")


@app.get("/user")
def user_get(request: Request,
             session: Annotated[Session, Depends(db_helper.get_db)]):
    user = check_token(session, request.cookies.get("token"))
    if user is None:
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    return templates.TemplateResponse("user.html", {"request": request, "user": user})


@app.post("/user")
def user_post(request: Request,
              session: Annotated[Session, Depends(db_helper.get_db)]):

    return {"Hello": "World"}


@app.get("/login")
def login_get(request: Request,
              session: Annotated[Session, Depends(db_helper.get_db)]):
    user = check_token(session, request.cookies.get("token"))
    if user is not None:
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login")
def login_post(request: Request,
               session: Annotated[Session, Depends(db_helper.get_db)],
               mail: str = Form(...), password: str = Form(...)):
    user = check_token(session, request.cookies.get("token"))
    if user is not None:
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    user = read_user_by_mail_password(session, mail, password)
    token = user.uuid
    response = RedirectResponse(url="/main", status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie(key="token", value=token, httponly=True, secure=True)
    return response


@app.get("/register")
def register_get(request: Request,
                 session: Annotated[Session, Depends(db_helper.get_db)]):
    user = check_token(session, request.cookies.get("token"))
    if user is not None:
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    return templates.TemplateResponse("register.html", {"request": request})


@app.post("/register")
def register_post(request: Request,
                  session: Annotated[Session, Depends(db_helper.get_db)],
                  fio: str = Form(...), address: str = Form(...),
                  phone: str = Form(...), mail: str = Form(...),
                  password: str = Form(...)):
    user = check_token(session, request.cookies.get("token"))
    if user is not None:
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    # todo exception with not enough params
    uid = uuid.uuid4()
    create_user(session, fio, address, mail, phone, password, 0, str(uid))
    return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/")
def main_page(request: Request,
              session: Annotated[Session, Depends(db_helper.get_db)]):
    lis = [{"name": "bow", "price": "10", "photo_id": 1}, {"name": "pan", "price": "100", "photo_id": 2}]
    return templates.TemplateResponse("main_page.html", {"request": request, "rents": lis})


@app.get("/rent")
def rent_get(request: Request,
             session: Annotated[Session, Depends(db_helper.get_db)]):

    return RedirectResponse(url="/main", status_code=status.HTTP_303_SEE_OTHER)


@app.post("/rent")
def rent_post(request: Request,
              session: Annotated[Session, Depends(db_helper.get_db)]):

    return {"Hello": "World"}
