# start.py
from chromadb.server.fastapi import FastAPIApp
import uvicorn

app = FastAPIApp()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
