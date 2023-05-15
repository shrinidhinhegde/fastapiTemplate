from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.database_config import get_database_session, Base
from src.env import env_variables
from src.main import server

APP_TEST_DATABASE_URL = f'postgresql://{env_variables.APP_DB_USER}:{env_variables.APP_DB_PASSWORD}@' \
                        f'{env_variables.APP_DB_HOST}:{env_variables.APP_DB_PORT}/{env_variables.APP_TEST_DB}'

engine = create_engine(APP_TEST_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_database_session():
    try:
        test_session = TestingSessionLocal()
        yield test_session
    finally:
        test_session.close()


server.dependency_overrides[get_database_session] = override_get_database_session
