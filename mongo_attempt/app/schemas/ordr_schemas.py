def findOrder(order) -> dict:
    return{
        "id": str(order["_id"]),
        "name": order["name"],
        "price": order["price"],
        "quantity": order["quantity"],
    }

def allOrders(orders) -> list:
    return[findOrder(order) for order in orders]