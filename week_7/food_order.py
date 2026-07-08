def calculate_total(price, quantity):
    if price < 0:
        raise ("invalid price")
    elif quantity < 0:
        raise ("invalid quantity")
    total = (quantity*price)
    return total
