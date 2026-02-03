FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY .env .env

ENV PYTHONPATH=/app/src

CMD ["uvicorn", "src.main.app:app", "--host", "0.0.0.0", "--port", "8000"]
