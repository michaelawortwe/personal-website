from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to my personal website"}

@app.get("/health")
def health():
    return {"status": "ok"}
