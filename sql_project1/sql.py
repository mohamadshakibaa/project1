from fastapi import APIRouter , Response
from pydantic import BaseModel 
from typing import Optional

router = APIRouter()


@router.get("/project1/sql")
async def data(name : Optional[str] = None , products : Optional[str] = None , price : Optional[int] = None):  

    Items = [
        {name : "labaniat" , products : [{name : "cheese" , id : 1 , price : "10000"}]},
        {name : "mavad shoyande" , products : [{name : "vitex" , id : 2 , price : "40000"}]},
        {name : "mavad behdashti" , products : [{name : "toothbrush" , id : 3 , price : "30000"}]},
        {name : "mavad qazaei" , products : [{name : "chicken" , id : 4 , price : "80000"}]},
        {name : "tanaqolat" , products : [{name : "peanut" , id : 5 , price : "60000"}]},
        {name : "drink" , products : [{name : "soda" , id : 6 , price : "20000"}]},
]
data()

