from fastapi import FastAPI , APIRouter

router = APIRouter()

@router.put("/project1/{id}")
def id(id : str):
    return{"message" : f" hello {id}"}