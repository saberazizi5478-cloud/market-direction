
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "status": "online",
        "project": "Market Direction",
        "version": "0.2"
    }


@app.get("/api/test")
def test():
    return {
        "success": True,
        "message": "Backend is ready"
    }
