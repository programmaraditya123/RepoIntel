from fastapi import FastAPI
# from app.routes import review

app = FastAPI()

# Root route
@app.get("/")
def home():
    return {"message": "AI Microservice is running"}

# Register routes
# app.include_router(review.router, prefix="/review")