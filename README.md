# COSMOCLOUD BACKEND INTERN HIRING TASK

Built using FastAPI and PostgreSQL


# FILE STRUCTURE

config.py has database parameter info taken from a .env file

database.py has the SQLAlchemy engine setup

models.py has the PostgreSQL table structure

schemas.py has the PyDantic BaseModels

main.py has the endpoints


#RUNNING LOCALLY

Pull "app" folder

Setup a postgres database with PGAdmin

Inside "app", create a .env file and provide all database information in that file as such:
```
DATABASE_PORT=5432
POSTGRES_PASSWORD=examplepassword
POSTGRES_USER=exampleusername
POSTGRES_DB=examplename
POSTGRES_HOST=examplehostname
POSTGRES_HOSTNAME=127.0.0.1
```

Create a virtual environment in same directory as "app"

Activate and install requirements.txt

Run using uvicorn as usual


# DATABASE DESIGN

Order is the model for orders. It has Address as a nested model and stores Items in a list of nested Items models

Product is the model for products. It is not connected to orders via relationship explicitly but via productid reference as instructed. Items model works as a pseudo many - to - many table

Address is the model for address. It is connected to Order via one - to - one relationship (ForeignKey). Created at the time of order creation

Items is the model that stores productid and boughtquantity


# ORDER VALIDATIONS AND PROPERTIES

Every itemid added to Items under product (as productid) is checked against existing Product database. Code proceeds only if match is found

Upon match, value of total is dynamically calculated by multiplying price of each product (accessed via productid) by boughtquantity and adding to a variable, which is ultimately added to Total column of Order

All APIs instructed in task are present in main.py
