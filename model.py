from typing import List, Optional

from sqlalchemy import Column, Float, ForeignKey, Integer, Text, create_engine
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship, sessionmaker
from sqlalchemy.orm.base import Mapped

Base = declarative_base()
metadata = Base.metadata


class DatabaseHelper:
    def __init__(self, url: str, echo: bool) -> None:
        self.engine = create_engine(url=url, echo=echo)
        self.session_make = sessionmaker(
            bind=self.engine
        )

    def get_db(self):
        with self.session_make() as session:
            try:
                yield session  # Provide the session to the caller
                session.commit()  # Commit if everything goes well
            except Exception as e:
                session.rollback()  # Rollback if an exception occurs
                raise e


db_helper = DatabaseHelper(url="sqlite:///reports.db", echo=False)


class Category(Base):
    __tablename__ = 'category'

    category_id = mapped_column(Integer, primary_key=True)
    name = mapped_column(Text, nullable=False)


class Users(Base):
    __tablename__ = 'users'

    user_id = mapped_column(Integer, primary_key=True)
    fio = mapped_column(Text)
    address = mapped_column(Text)
    mail = mapped_column(Text)
    phone_number = mapped_column(Text)
    password = mapped_column('pass', Text)
    rating = mapped_column(Float)
    uuid = mapped_column(Text)

    rent: Mapped[List['Rent']] = relationship('Rent', uselist=True, back_populates='user')
    chat: Mapped[List['Chat']] = relationship('Chat', uselist=True, back_populates='user')


class Rent(Base):
    __tablename__ = 'rent'

    rent_id = mapped_column(Integer, primary_key=True)
    user_id = mapped_column(ForeignKey('users.user_id'), nullable=False)
    name = mapped_column(Text)
    price = mapped_column(Text)
    description = mapped_column(Text)

    user: Mapped['Users'] = relationship('Users', back_populates='rent')
    chat: Mapped[List['Chat']] = relationship('Chat', uselist=True, back_populates='rent')
    photo: Mapped[List['Photo']] = relationship('Photo', uselist=True, back_populates='rent')
    rent_category: Mapped[List['RentCategory']] = relationship('RentCategory', uselist=True, back_populates='rent')


class Chat(Base):
    __tablename__ = 'chat'

    chat_id = mapped_column(Integer, primary_key=True)
    user_id = mapped_column(ForeignKey('users.user_id'))
    rent_id = mapped_column(ForeignKey('rent.rent_id'))

    rent: Mapped[Optional['Rent']] = relationship('Rent', back_populates='chat')
    user: Mapped[Optional['Users']] = relationship('Users', back_populates='chat')
    chat_massage: Mapped[List['ChatMassage']] = relationship('ChatMassage', uselist=True, back_populates='chat')


class Photo(Base):
    __tablename__ = 'photo'

    photo_id = mapped_column(Integer, primary_key=True)
    num = mapped_column(Integer, nullable=False)
    rent_id = mapped_column(ForeignKey('rent.rent_id'), nullable=False)

    rent: Mapped['Rent'] = relationship('Rent', back_populates='photo')


class RentCategory(Category):
    __tablename__ = 'rent_category'

    rent_category_id = mapped_column(Integer, nullable=False)
    category_id = mapped_column(ForeignKey('category.category_id'), primary_key=True)
    rent_id = mapped_column(ForeignKey('rent.rent_id'))

    rent: Mapped[Optional['Rent']] = relationship('Rent', back_populates='rent_category')


class ChatMassage(Base):
    __tablename__ = 'chat_massage'

    chat_massage_id = mapped_column(Integer, primary_key=True)
    chat_id = mapped_column(ForeignKey('chat.chat_id'))
    who = mapped_column(Integer)

    chat: Mapped[Optional['Chat']] = relationship('Chat', back_populates='chat_massage')
