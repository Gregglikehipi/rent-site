import uuid
from typing import Union, Optional, List, Annotated

from sqlalchemy.orm import Session

from logic import check_token

from fastapi import FastAPI, Request, Depends, status, Form, File, UploadFile, HTTPException
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
        return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)
    flag = 1
    if user is None:
        flag = 0
    return templates.TemplateResponse("user.html", {"request": request, "user": user, "flag": flag})


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
    if user is None:
        return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)
    token = user.uuid
    response = RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie(key="token", value=token, httponly=True, secure=True)
    return response

@app.get("/logout")
def logout(request: Request,
          session: Annotated[Session, Depends(db_helper.get_db)]):
    response = RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    response.delete_cookie("token")
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
                  password: str = Form(...), telegram: str = Form(...),
                  student_id: str = Form(...)):
    user = check_token(session, request.cookies.get("token"))
    if user is not None:
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    # todo exception with not enough params
    uid = uuid.uuid4()
    create_user(session, fio, address, mail, phone, password, 0, str(uid), telegram, student_id)
    return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/")
def main_page(request: Request,
              session: Annotated[Session, Depends(db_helper.get_db)]):
    user = check_token(session, request.cookies.get("token"))
    rents = read_rents(session)
    flag = 1
    if user is None:
        flag = 0
    return templates.TemplateResponse("main_page.html", {"request": request, "rents": rents, "flag": flag})


@app.get("/rent/{item_id}")
def rent_get(request: Request,
             session: Annotated[Session, Depends(db_helper.get_db)],
             item_id: int):
    user = check_token(session, request.cookies.get("token"))
    flag = 1
    if user is None:
        flag = 0
    rent = read_rent(session, item_id)
    photo = read_photo_with_rent_id(session, rent.rent_id)
    rent_user = read_user(session, rent.user_id)
    return templates.TemplateResponse("rent_page.html", {"request": request, "rent": rent, "photo": photo, "flag": flag, "user": rent_user})


@app.get("/rentcreate")
def rent_create_get(request: Request,
                    session: Annotated[Session, Depends(db_helper.get_db)]):
    user = check_token(session, request.cookies.get("token"))
    flag = 1
    if user is None:
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    return templates.TemplateResponse("rent_add.html", {"request": request, "flag": flag})


@app.post("/rentcreate")
async def rent_create_post(request: Request,
                           session: Annotated[Session, Depends(db_helper.get_db)],
                           photos: list[UploadFile],
                           name: str = Form(...), price: str = Form(...),
                           address: str = Form(...), description: str = Form(...)):
    user = check_token(session, request.cookies.get("token"))
    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    r_id = create_rent(session, user.user_id, name, price, description, address)

    i = 1
    for photo in photos:
        photo_id = create_photo(session, i, r_id)
        name = str(photo_id) + ".png"
        dirk = f"static/photo/{name}"
        with open(dirk, "wb") as f:
            content = await photo.read()
            f.write(content)
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

@app.get("/test2")
def test2(request: Request,
          session: Annotated[Session, Depends(db_helper.get_db)]):
    user = check_token(session, request.cookies.get("token"))
    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return templates.TemplateResponse("test2.html", {"request": request, "user_id": user.user_id})


@app.get("/tes")
def test2(request: Request,
          session: Annotated[Session, Depends(db_helper.get_db)]):
    return templates.TemplateResponse("df.html", {"request": request})