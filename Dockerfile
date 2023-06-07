FROM python:latest

LABEL authors="Shrinidhi Hegde"

WORKDIR /server

RUN pip install poetry

COPY README.md poetry_utils.py pyproject.toml ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY src ./src

ENV PYTHONPATH "${PYTHONPATH}:/server"

WORKDIR /server/src

CMD ["python3", "main.py"]