# this select query is used to change data from data of neon database
from sqlalchemy.orm import Session
from sqlalchemy import select
from connection import engine

from create_user import User


session = Session(engine)

stmt = select(User).where(User.name.in_(["bushra", "sandy"]))

for user in session.scalars(stmt):
    print(user)