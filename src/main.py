import os

import uvicorn
from dotenv import dotenv_values, load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

server = FastAPI(title='Application Title',
                 description='Application Description. Add more details here. Takes in Markdown format as well.')

server.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"],
                      allow_headers=["*"], )


@server.get("/", tags=["App Root"])
def root():
    return {"message": "Welcome to App Backend"}


@server.get("/health", tags=["App Root"])
def health():
    return {"message": "OK"}


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
