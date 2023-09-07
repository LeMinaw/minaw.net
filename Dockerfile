ARG PYTHON_VERSION=3.10-slim-bullseye

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code
COPY . /code
WORKDIR /code

RUN pip install pdm
RUN pdm sync --no-self

RUN pdm run manage.py collectstatic --noinput

EXPOSE 8000

CMD ["./bin/launch.sh"]
