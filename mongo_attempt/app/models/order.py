from datetime import datetime
from pydantic import BaseModel
from models.address import Address
from models.product import Product
from bson import ObjectId

class Order(BaseModel):
    timestamp: datetime
    products: list[ObjectId]
    total: int
    address: ObjectId

    class Config:
        json_encoders = {
            ObjectId: lambda v: str(v),
        }