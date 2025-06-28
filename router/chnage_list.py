from fastapi import APIRouter 
from typing import Literal, Optional
from pydantic import BaseModel

router = APIRouter()

class Items(BaseModel): 
    name : str
    description : Optional[str] = None
    price : float
    products : Optional[list[dict]] = None


items = {
        "labaniat" : {"name" : "labaniat" ,"description": "milk"  , "price" : 10000, "products" : [{"name" : "cheese" , "id" : 1}]},
        "mavad_shoyande" : {"name" : "mavad_shoyande" ,"description": "none" , "price" : 40000, "products" : [{"name" : "vitex" , "id" : 2 }]},
        "mavad_behdashti" : {"name" : "mavad_behdashti" ,"description": "dastmal" , "price" : 30000, "products" : [{"name" : "toothbrush" , "id" : 3 }]},
        "mavad_qazaei" : {"name" : "mavad_qazaei" ,"description": "fish" , "price" : 80000, "products" : [{"name" : "chicken" , "id" : 4 }]},
        "tanaqolat" : {"name" : "tanaqolat" ,"description": "peste"  , "price" : 60000, "products" : [{"name" : "peanut" , "id" : 5}]},
        "drink" : {"name" : "drink" ,"description": "soda" , "price" : 20000, "products" : [{"name" : "soda" , "id" : 6 }]}
}


@router.post('/itmes' , response_model= Items , tags=["change list"])
          
async def create_exclude(item : Items):
    
    return item
