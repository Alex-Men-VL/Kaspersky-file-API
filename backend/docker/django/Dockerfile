FROM python:3.11.4-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code
ARG APP_ROOT=/code

RUN apt-get update  && \
    apt install -y python3-dev \
    libboost-mpi-python-dev \
    gcc \
    musl-dev \
    libpq-dev postgresql postgresql-contrib \
    default-jre libreoffice-java-common \
    libreoffice --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install poetry==1.6.1

COPY ./backend/pyproject.toml ./

RUN poetry config virtualenvs.create false \
    && poetry install

COPY ./backend/docker/django/entrypoint.sh /docker-entrypoint.sh
RUN chmod +x '/docker-entrypoint.sh'

COPY ./backend/src ${APP_ROOT}

ENTRYPOINT ["/docker-entrypoint.sh"]
