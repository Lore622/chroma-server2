# start.py
import chromadb
from chromadb.config import Settings
import uvicorn
import os

# Configurazione del server
server_settings = Settings(
    chroma_api_impl="rest",
    chroma_server_host="0.0.0.0",
    chroma_server_port=int(os.environ.get("PORT", 8000)),
    chroma_server_cors_allow_origins=["*"],
    persist_directory="chroma_data",  # Per persistere i dati
    allow_reset=True
)

# Avvia il server
server = chromadb.Server(server_settings)

if __name__ == "__main__":
    server.run()
