from fastapi import APIRouter
from models.product import Product
from config.database import prod_coll
from schemas.prod_schemas import allProducts
from bson import ObjectId

prod_router = APIRouter()

@prod_router.get("/product/")
async def get_products():
    products = allProducts(prod_coll.find())
    return products

@prod_router.post("/product/")
async def post_product(product: Product):
    prod_coll.insert_one(dict(product))

@prod_router.put("/product/{id}")
async def update_product(id: str, product: Product):
    prod_coll.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(product)})

@prod_router.delete("/product/{id}")
async def delete_product(id: str, product: Product):
    prod_coll.find_one_and_delete({"_id": ObjectId(id)})
