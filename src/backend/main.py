from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve React build if it exists
react_build_dir = os.path.join(os.path.dirname(__file__), '..', 'frontend', 'build')
if os.path.isdir(react_build_dir):
    app.mount("/", StaticFiles(directory=react_build_dir, html=True), name="static")

@app.get("/api/hello")
def read_root():
    return {"message": "Hello, World!"} 