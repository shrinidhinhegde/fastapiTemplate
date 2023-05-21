import asyncio

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from src.database_config import get_database_session, Base
from src.env_config.env import env_variables
from src.main import server

APP_TEST_DATABASE_URL = (
    f"postgresql+asyncpg://{env_variables.APP_DB_USER}:{env_variables.APP_DB_PASSWORD}@"
    f"{env_variables.APP_DB_HOST}:{env_variables.APP_DB_PORT}/{env_variables.APP_TEST_DB}"
)

engine = create_async_engine(APP_TEST_DATABASE_URL, future=True, echo=True)

TestingSessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


asyncio.run(init_models())


def override_get_database_session():
    try:
        test_session = TestingSessionLocal()
        yield test_session
    finally:
        test_session.close()


server.dependency_overrides[get_database_session] = override_get_database_session
