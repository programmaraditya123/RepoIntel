from fastapi import APIRouter
from app.api.v1.endpoints import commit

api_router = APIRouter()

api_router.include_router(commit.router,prefix="/commit",tags=["Users"])