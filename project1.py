from fastapi import FastAPI
from router import general , chnage_list , give_product
from sql_project1 import sql



app = FastAPI()
app.include_router(general.router)
app.include_router(chnage_list.router)
app.include_router(give_product.router)
app.include_router(sql.router)

# uvicorn project1:app --reload 