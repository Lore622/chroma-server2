FROM python:3.10-slim

WORKDIR /app

# Aggiorna pip e installa le dipendenze
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia il codice dell'applicazione
COPY . .

# Crea la directory per i dati persistenti
RUN mkdir -p chroma_data

# Esponi la porta
ENV PORT=8000
EXPOSE 8000

# Avvia l'applicazione
CMD ["python", "start.py"]
