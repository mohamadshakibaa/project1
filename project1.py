from fastapi import FastAPI , APIRouter
from router import router_get, router_post , router_put
from sql_project1 import sql



app = FastAPI()
app.include_router(router_get.router)
app.include_router(router_post.router)
app.include_router(router_put.router)
app.include_router(sql.router)

# uvicorn project1:app --reload 