from fastapi import APIRouter

router = APIRouter()

@router.put("/project1/{id}" , tags=[" give product"])
def id(id : str):
    return{"message" : f" {id} is not exist "}