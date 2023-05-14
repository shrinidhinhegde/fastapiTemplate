from sqlalchemy import String, Column

from src.database_config import Base


class MyModel(Base):
    __tablename__ = "my_model"

    primary_key_column = Column(String, primary_key=True)
    test_column = Column(String)
