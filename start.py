# start.py
import chromadb
from chromadb.config import Settings
import uvicorn

# Create server instance
settings = Settings(
    chroma_server_host="0.0.0.0",
    chroma_server_port=8000,
    chroma_server_cors_allow_origins=["*"],
    allow_reset=True,
    anonymized_telemetry=False
)

server = chromadb.Server(settings)

if __name__ == "__main__":
    server.run()
