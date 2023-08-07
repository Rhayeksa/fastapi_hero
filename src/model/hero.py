from sqlalchemy import Column, DateTime, Integer, String

from src.config.database import Base


class Hero(Base):
    __tablename__ = "hero"

    id = Column(Integer, primary_key=True, index=True, autoincrement="auto")
    name = Column(String(45), unique=True, nullable=False)
    type = Column(String(25), nullable=False)
    description = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
