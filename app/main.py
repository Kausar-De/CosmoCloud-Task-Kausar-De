from fastapi import FastAPI, HTTPException, Depends
import models
import schemas
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind = engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
#Order Endpoints
@app.post('/order/')
async def create_order(order: schemas.OrderBase, db: Session = Depends(get_db)):
    db_order = models.Order(time_stamp = order.time_stamp)
    db_address = models.Address(city = order.address.city, country = order.address.country, zipcode = order.address.zipcode, order_id = db_order.id)
    db.add(db_address)
    itemids = [i.id for i in db.query(models.Product.id)]
    prodtotal = 0.0 
    print(itemids)
    for item in order.items:
        db_item = models.Items(productid = item.productid, boughtqty = item.boughtqty, order_id = db_order.id)
        if db_item.productid not in itemids:
            raise HTTPException(status_code = 404, detail = "Item of given ID not in Products!")
        val = db.query(models.Product).filter(models.Product.id == db_item.productid).first()
        if db_item.boughtqty > val.quantity:
            raise HTTPException(status_code = 400, detail = "Number of products exceeds stock!")
        prodtotal += val.price * db_item.boughtqty
        print(prodtotal)
    db.add(db_item)
    db_order.total = prodtotal
    db.add(db_order)
    db.commit()


@app.get('/order/')
async def get_all_orders(db: Session = Depends(get_db), skip: int = 0, limit: int = 5):
    result = db.query(models.Order).offset(skip).limit(limit).all()
    if not result:
        raise HTTPException(status_code = 404, detail = "No Orders in system!")
    return result

@app.get('/order/{order_id}')
async def get_order_by_id(order_id: int, db: Session = Depends(get_db)):
    result = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not result:
        raise HTTPException(status_code = 404, detail = "Order of given ID not found!")
    return result


#Address Endpoints
@app.get('/address/{order_id}')
async def get_address_by_id(order_id: int, db: Session = Depends(get_db)):
    result = db.query(models.Address).filter(models.Order.id == order_id).first()
    return result


#Product Endpoints
@app.post('/product/')
async def create_product(product: schemas.ProductBase, db: Session = Depends(get_db)):
    db_product = models.Product(name = product.name, price = product.price, quantity = product.quantity)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

@app.get('/product/')
async def get_all_products(db: Session = Depends(get_db), skip: int = 0, limit: int = 5):
    result = db.query(models.Product).offset(skip).limit(limit).all()
    if not result:
        raise HTTPException(status_code = 404, detail = "No Products in system!")
    return result

@app.put('/product/{product_id}')
async def update_product(product_id: int, product: schemas.ProductBase, db: Session = Depends(get_db)):
    result = db.query(models.Product).filter(models.Product.id == product_id).first()
    result.name = product.name
    result.price = product.price
    result.quantity = product.quantity
    db.commit()
    db.refresh(result)
    