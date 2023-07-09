from sqlalchemy import Column, ForeignKey, Integer, String, Float, TIMESTAMP, text
from sqlalchemy.orm import relationship
from database import Base

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key = True, index = True)
    time_stamp = Column(TIMESTAMP(timezone = True), server_default = text("now()"))
    total = Column(Float)
    address = relationship("Address", back_populates = "order")
    items = relationship("Items", back_populates = "order")

class Items(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key = True, index = True)
    productid = Column(Integer)
    boughtqty = Column(Integer)
    order_id = Column(Integer, ForeignKey('orders.id'))
    order = relationship("Order", back_populates = "items")    

class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key = True, index = True)
    city = Column(String)
    country = Column(String)
    zipcode = Column(Integer)
    order_id = Column(Integer, ForeignKey('orders.id'))
    order = relationship("Order", back_populates = "address")

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    price = Column(Float)
    quantity = Column(Integer)