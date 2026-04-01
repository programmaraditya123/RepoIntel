from fastapi import FastAPI
from app.aimodels.geminiModel import get_gemini_llm

from app.api.v1.api import api_router
 

app = FastAPI()
llm = get_gemini_llm()

app.include_router(api_router,prefix='/api/v1')

# Root route
@app.get("/")
def home():
    return {"message": "Microservice is running"}

@app.get("/health")
def health():
    return {"status" : "ok"}
