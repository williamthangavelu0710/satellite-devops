from fastapi import FastAPI

app = FastAPI(title="Satellite Ground Station Management API")

@app.get("/")
def home():
    return {"message": "Satellite Ground Station Platform"}

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "ground-station-management-api"
    }
