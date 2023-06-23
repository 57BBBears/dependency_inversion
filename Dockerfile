FROM python:3.11.4-alpine3.18

ARG APP_ENV=development

ENV APP_ENV=$APP_ENV
ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONHASHSEED=random
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100
ENV POETRY_VERSION=1.5

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /dependency_inversion
COPY poetry.lock pyproject.toml /dependency_inversion/
RUN poetry config virtualenvs.create false \
  && poetry install $(test "$APP_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

COPY . /dependency_inversion/
