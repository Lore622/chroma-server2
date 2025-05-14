# start.py
import os
from chromadb.server import ChromaServer

# Configura la porta - Render ti assegnerà una porta tramite variabile d'ambiente
port = int(os.environ.get("PORT", 8000))

# Avvia il server
server = ChromaServer(
    host="0.0.0.0",
    port=port,
    ssl_enabled=False,
    persist_directory="chroma_data",  # directory per dati persistenti
    allow_reset=True,
    cors_allow_origins=["*"]
)

if __name__ == "__main__":
    server.run()
