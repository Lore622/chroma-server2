FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install chromadb==0.4.24


EXPOSE 8000

CMD ["python", "start.py"]

