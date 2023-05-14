import os

import uvicorn
from dotenv import dotenv_values, load_dotenv
from fastapi import FastAPI

server = FastAPI(title='Application Title',
                 description='Application Description. Add more details here. Takes in Markdown format as well.')


@server.get("/", tags=["App Root"])
def root():
    return {"message": "Welcome to App Backend"}


@server.get("/health", tags=["App Root"])
def health():
    return {"message": "OK"}


load_dotenv()  # for EnvironmentVariables class


class EnvironmentVariables:
    APP_DB = os.getenv("POSTGRES_DB")
    APP_DB_USER = os.getenv("POSTGRES_USER")
    APP_DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    APP_DB_HOST = os.getenv("POSTGRES_HOST")
    APP_DB_PORT = os.getenv("POSTGRES_PORT")
    # any other environment variables you want to use in your application


env_variables = EnvironmentVariables()

if __name__ == "__main__":
    env_vars = list(dotenv_values('.env.example').keys())

    load_dotenv()
    try:
        for var in env_vars:
            x = os.environ[var]
    except KeyError as e:
        print(f"Please set the environment variable {e}. Application must contain {env_vars}")
        exit(1)
    uvicorn.run("main:server", host="0.0.0.0", port=8000, reload=True)
