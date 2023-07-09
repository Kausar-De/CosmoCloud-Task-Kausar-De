from pydantic import BaseModel

class Address(BaseModel):
    city: str
    country: str
    zipcode: int