FROM python:3.10-slim

WORKDIR /app

COPY . /app

ENV PYTHONPATH=/app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["pytest", "--maxfail=1", "--disable-warnings", "-v", "tests"]