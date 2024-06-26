FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN [ "pip", "install", "-r", "requirements.txt" ]

COPY app /app

ENTRYPOINT [ "python3", "main.py" ]