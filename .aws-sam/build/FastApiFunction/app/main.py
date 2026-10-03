from fastapi import FastAPI
from mangum import Mangum
from app.api import auth, profile

app = FastAPI(title="Cognito Auth & DynamoDB Service", version="1.0.0")

app.include_router(auth.router)
app.include_router(profile.router)

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# AWS Lambda ke liye entry handler
handler = Mangum(app)