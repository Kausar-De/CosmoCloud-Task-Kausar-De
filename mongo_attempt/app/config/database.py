from pymongo import MongoClient

client = MongoClient("mongodb+srv://hidden:hidden@hidden.hidden.mongodb.net/?retryWrites=true&w=majority")

db = client.product_db

prod_coll = db["product_collection"]
addr_coll = db["address_collection"]
ordr_coll = db["order_collection"]