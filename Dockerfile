from python:3.10.13-slim


COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -r /app/requirements.txt
