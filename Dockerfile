FROM python:3.10-slim

WORKDIR /app

# Installa le dipendenze
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia il codice dell'applicazione
COPY . .

# Crea la directory per i dati persistenti
RUN mkdir -p chroma_data

# Esponi la porta su cui il server ChromaDB ascolterà
EXPOSE 8000

# Avvia l'applicazione
CMD ["python", "start.py"]
