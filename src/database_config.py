from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.main import env_variables

APP_DATABASE_URL = f'postgresql://{env_variables.APP_DB_USER}:{env_variables.APP_DB_PASSWORD}@' \
                   f'{env_variables.APP_DB_HOST}:{env_variables.APP_DB_PORT}/{env_variables.APP_DB}'

engine = create_engine(APP_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_database_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
