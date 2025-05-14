# start.py
import chromadb
from chromadb.config import Settings
import uvicorn

# Configurazione del server ChromaDB
chroma_server = chromadb.Server(Settings(
    chroma_api_impl="chromadb.api.fastapi.FastAPI",
    chroma_server_host="0.0.0.0",
    chroma_server_port=8000
))

if __name__ == "__main__":
    chroma_server.run()
