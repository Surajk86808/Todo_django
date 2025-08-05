# app/notes/models.py
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from app.db.base import Base

class Note(Base):
    __tablename__ = "notes"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)
