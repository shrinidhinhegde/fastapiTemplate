from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from src.env_config.env import env_variables

APP_DATABASE_URL = (
    f"postgresql+asyncpg://{env_variables.APP_DB_USER}:{env_variables.APP_DB_PASSWORD}@"
    f"{env_variables.APP_DB_HOST}:{env_variables.APP_DB_PORT}/{env_variables.APP_DB}"
)

engine = create_async_engine(APP_DATABASE_URL, future=True, echo=True)

SessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()


def get_database_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
