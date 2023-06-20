FROM python:3.10-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install poetry && poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml ./

RUN poetry install

COPY src ./

COPY entrypoint.sh ./

ENTRYPOINT ["./entrypoint.sh"]

# FROM python:3.10-slim

# WORKDIR /app

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# RUN apt-get update && \ 
#     apt-get install -y --no-install-recommends libpq-dev

# RUN apt-get install -y --no-install-recommends python3-dev gcc curl

# RUN pip install poetry && poetry config virtualenvs.create false

# COPY poetry.lock pyproject.toml ./

# RUN poetry install

# COPY src ./