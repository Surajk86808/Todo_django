# app/db/config.py
import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
db_path = os.path.join(BASE_DIR, "sqlite.db")  # 🛠️ Fix: you had `os.path.jion` (typo)

DATABASE_URL = f"sqlite+aiosqlite:///{db_path}"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)
