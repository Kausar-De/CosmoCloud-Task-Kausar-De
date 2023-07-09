from fastapi import FastAPI
from routes.prod_route import prod_router
from routes.addr_route import addr_router
from routes.ordr_route import ordr_router

app = FastAPI()
app.include_router(prod_router)
app.include_router(addr_router)
app.include_router(ordr_router)
