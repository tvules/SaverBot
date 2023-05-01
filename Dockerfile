FROM python:3.10-slim

WORKDIR /app

COPY tgbot/ tgbot/
COPY alembic/ alembic/
COPY alembic.ini .
COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

CMD ["sh", "-c", "alembic upgrade head && python -m tgbot"]
