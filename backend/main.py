from fastapi import FastAPI

app = FastAPI(title="Career AI API")

@app.get("/")
def root():
    return {"message": "Career AI backend is running"}
