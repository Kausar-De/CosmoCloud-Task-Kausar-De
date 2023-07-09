from fastapi import APIRouter
from models.order import Order
from config.database import ordr_coll
from schemas.ordr_schemas import allOrders
from bson import ObjectId

ordr_router = APIRouter()

@ordr_router.get("/order/")
async def get_orders():
    orders = allOrders(ordr_coll.find())
    return orders

@ordr_router.post("/order/")
async def post_order(order: Order):
    ordr_coll.insert_one(dict(order))

@ordr_router.put("/order/{id}")
async def update_order(id: str, order: Order):
    ordr_coll.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(order)})

@ordr_router.delete("/order/{id}")
async def delete_order(id: str, order: Order):
    ordr_coll.find_one_and_delete({"_id": ObjectId(id)})
