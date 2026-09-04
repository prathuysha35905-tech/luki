from recommend import search_movie, recommend_movie
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pathlib import Path
from fastapi.responses import FileResponse


BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_FILE = BASE_DIR / "frontend" / "index.html"


app = FastAPI(title="Netflix AI Recommendation System")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    return FileResponse(FRONTEND_FILE)

@app.get("/models")
def models():
    response = requests.get("http://127.0.0.1:1234/v1/models")
    return response.json()

@app.get("/search/{movie}")
def search(movie: str):
    return search_movie(movie)

@app.get("/recommend/{movie}")
def recommend(movie: str):
    return recommend_movie(movie)