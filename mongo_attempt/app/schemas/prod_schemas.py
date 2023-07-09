def findProduct(product) -> dict:
    return{
        "id": str(product["_id"]),
        "name": product["name"],
        "price": product["price"],
        "quantity": product["quantity"],
    }

def allProducts(products) -> list:
    return[findProduct(product) for product in products]