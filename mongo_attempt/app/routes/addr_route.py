from fastapi import APIRouter
from models.address import Address
from config.database import addr_coll
from schemas.addr_schemas import allAddresses
from bson import ObjectId

addr_router = APIRouter()

@addr_router.get("/address/")
async def get_addresss():
    addresss = allAddresses(addr_coll.find())
    return addresss

@addr_router.post("/address/")
async def post_address(address: Address):
    addr_coll.insert_one(dict(address))

@addr_router.put("/address/{id}")
async def update_address(id: str, address: Address):
    addr_coll.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(address)})

@addr_router.delete("/address/{id}")
async def delete_address(id: str, address: Address):
    addr_coll.find_one_and_delete({"_id": ObjectId(id)})
