import os

import uvicorn
from celery import Celery
from dotenv import dotenv_values, load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from celery_tasks import tasks
from env_config.env import env_variables

# FastAPI Configuration
server = FastAPI(
    title="Application Title",
    description="Application Description. Add more details here. Takes in Markdown format as well.",
)
server.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Celery Configuration
celery = Celery(
    __name__,
    broker=f"redis://{env_variables.REDIS_HOST}:{env_variables.REDIS_PORT}/0",
    backend=f"redis://{env_variables.REDIS_HOST}:{env_variables.REDIS_PORT}/0",
)
celery.conf.imports = [
    "celery_tasks.tasks",
    # more tasks here
]


# to run migrations from sqlalchemy
# @server.on_event("startup")
# async def init_tables():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)


# Routes
@server.get("/", tags=["App Root"])
async def root():
    return {"message": "Welcome to App Backend"}


@server.get("/health", tags=["App Root"])
async def health():
    tasks.test_shared_task.delay()
    return {"message": "OK"}


if __name__ == "__main__":
    env_vars = list(dotenv_values("env_config/.env.example").keys())

    load_dotenv()
    try:
        for var in env_vars:
            x = os.environ[var]
    except KeyError as e:
        print(
            f"Please set the environment variable {e}. Application must contain all the environment variables in "
            f".env.example"
        )
        exit(1)
    uvicorn.run("main:server", host="0.0.0.0", port=8000, reload=True)
