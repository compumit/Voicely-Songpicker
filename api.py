from fastapi import FastAPI app = FastAPI() @app.get("/") def home():
    return {"message": "VocalCoach API is running!"} @app.get("/search_songs") def search_songs(): return {"songs": "This will return a list of songs"}

