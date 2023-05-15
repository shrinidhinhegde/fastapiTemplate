import os

from dotenv import load_dotenv

load_dotenv()


class EnvironmentVariables:
    APP_DB = os.getenv("POSTGRES_DB")
    APP_DB_USER = os.getenv("POSTGRES_USER")
    APP_DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    APP_DB_HOST = os.getenv("POSTGRES_HOST")
    APP_DB_PORT = os.getenv("POSTGRES_PORT")
    APP_TEST_DB = os.getenv("POSTGRES_TEST_DB")
    # any other environment variables you want to use in your application


env_variables = EnvironmentVariables()
