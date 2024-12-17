from model import *


def create_rent(session, user_id, name, price, description, address):
    data = Rent(user_id=user_id, name=name, price=price, description=description, address=address)
    session.add(data)
    session.flush()  # Flush the changes to the database
    session.refresh(data)
    r_id = data.rent_id
    return r_id


def read_rents(session):
    data = session.query(Rent).all()
    return data

def read_rent(session, rent_id):
    data = session.query(Rent).filter_by(rent_id=rent_id).first()
    return data


def update_rent(session, rent_id, user_id, name, price, description, address):
    data = session.query(Rent).filter_by(rent_id=rent_id).first()

    if data:
        if user_id:
            data.user_id = user_id
        if name:
            data.name = name
        if price:
            data.price = price
        if description:
            data.description = description
        if address:
            data.role_text = address
    else:
        print(f"ID {rent_id} не найдено.")


def delete_rent(session, rent_id):
    data = session.query(Rent).filter_by(rent_id=rent_id).first()

    if data:
        session.delete(data)
    else:
        print(f"ID {rent_id} не найдено.")


def create_user(session, fio, address, mail, phone_number, password, rating, uuid, telegram, student_id):
    data = Users(fio=fio, address=address, mail=mail, phone_number=phone_number, password=password,
                 rating=rating, uuid=uuid, telegram=telegram, student_id=student_id)
    session.add(data)


def read_users(session):
    data = session.query(Users).all()
    return data

def read_user(session, user_id):
    data = session.query(Users).filter_by(user_id=user_id).first()
    return data

# todo


def update_user(session, role_id, role_text=None, access_level=None):
    data = session.query(Users).filter_by(role_id=role_id).first()

    if data:
        if role_text:
            data.role_text = role_text
        if access_level:
            data.access_level = access_level
    else:
        print(f"Пользователь с ID {role_id} не найден.")


def delete_user(session, role_id):
    data = session.query(Users).filter_by(role_id=role_id).first()

    if data:
        session.delete(data)
    else:
        print(f"ID {role_id} не найдено.")


def read_user_by_uuid(session, uuid):
    data = session.query(Users).filter_by(uuid=uuid).first()

    return data


def read_user_by_mail_password(session, mail, password):
    user = session.query(Users).filter_by(mail=mail, password=password).first()

    return user


def create_photo(session, num, rent_id):
    data = Photo(num=num, rent_id=rent_id)
    session.add(data)
    session.flush()
    session.refresh(data)
    r_id = data.photo_id
    return r_id

def read_photos(session):
    data = session.query(Photo).all()
    return data

def read_photo_with_rent_id(session, rent_id):
    data = session.query(Photo).filter_by(rent_id=rent_id).first()
    return data

def delete_photo(session, photo_id):
    data = session.query(Photo).filter_by(photo_id=photo_id).first()

    if data:
        session.delete(data)
    else:
        print(f"ID {photo_id} не найдено.")

