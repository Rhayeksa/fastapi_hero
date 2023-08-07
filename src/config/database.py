from os import environ

from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

env = dotenv_values(".env")

USERNAME = environ.get("DB_USERNAME") if environ.get(
    "DB_USERNAME") != None else env["DB_USERNAME"]
PASSWORD = environ.get("DB_PASSWORD") if environ.get(
    "DB_PASSWORD") != None else env["DB_PASSWORD"]
IP = environ.get("DB_IP") if environ.get(
    "DB_IP") != None else env["DB_IP"]
PORT = environ.get("DB_PORT") if environ.get(
    "DB_PORT") != None else env["DB_PORT"]
DB = environ.get("DB") if environ.get(
    "DB") != None else env["DB"]
URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{IP}:{PORT}/{DB}"


class Base(DeclarativeBase):
    pass


engine = create_engine(url=URI, pool_pre_ping=True)
session = sessionmaker(bind=engine)
session = session()
