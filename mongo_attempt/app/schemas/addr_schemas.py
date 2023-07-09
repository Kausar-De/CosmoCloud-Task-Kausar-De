def findAddress(address) -> dict:
    return{
        "id": str(address["_id"]),
        "city": address["city"],
        "country": address["country"],
        "zipcode": address["zipcode"],
    }

def allAddresses(addresses) -> list:
    return[findAddress(address) for address in addresses]