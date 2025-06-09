from fastapi import FastAPI , APIRouter 


router = APIRouter()

@router.get("/project1/")
def get():
    return{"message" : "hello "}