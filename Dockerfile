FROM python:3.10-slim

WORKDIR /app

RUN pip install chromadb

EXPOSE 8000

CMD ["chromadb", "run", "--host", "0.0.0.0", "--port", "8000"]

