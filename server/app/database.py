import os
from contextlib import contextmanager

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import CreateTable
from dotenv import load_dotenv

load_dotenv()

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/metricvn"


SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://DetailProduct_owner:SyA9nz3fmOFC@ep-lingering-sunset-a1dumh0h.ap-southeast-1.aws.neon.tech/DetailProduct"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

# Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
