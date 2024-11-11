from model import *


def create_rent(user_id, name, price, description):
    session = Session()
    new_rent = Rent(user_id=user_id, name=name, price=price, description=description)
    session.add(new_rent)
    session.commit()
    session.close()


def read_rents():
    session = Session()
    rents = session.query(Rent).all()
    session.close()
    return rents


def update_rent(role_id, role_text=None, access_level=None):
    session = Session()
    role = session.query(Rent).filter_by(role_id=role_id).first()

    if role:
        if role_text:
            role.role_text = role_text
        if access_level:
            role.access_level = access_level
        session.commit()
    else:
        print(f"Пользователь с ID {role_id} не найден.")

    session.close()


def delete_rent(role_id):
    session = Session()
    role = session.query(Rent).filter_by(role_id=role_id).first()

    if role:
        session.delete(role)
        session.commit()
    else:
        print(f"Пользователь с ID {role_id} не найден.")

    session.close()