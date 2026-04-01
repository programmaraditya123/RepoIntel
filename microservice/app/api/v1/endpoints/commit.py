from fastapi import APIRouter


router = APIRouter();

@router.get("/explain")
def generate():
    print("hello")