FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY main.py .
COPY app ./app
# COPY .env .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
