from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Adaptive AI Command Center Running"}