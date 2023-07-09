from pydantic import BaseModel, Field
from datetime import datetime

class AddressBase(BaseModel):
    city: str
    country: str
    zipcode: int

class OrderItem(BaseModel):
    productid: int
    boughtqty: int

class OrderBase(BaseModel):
    time_stamp: datetime
    address: AddressBase
    items: list[OrderItem]

class ProductBase(BaseModel):
    name: str
    price: float
    quantity: int