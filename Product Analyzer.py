

products={'apple': 10,
         'banana': 15,
         'milk': 30,
         'bread': 25}



def total_price(products):
    total = 0

    for price in products.values():
        total+= price

    return (total)





def most_expensive(products):
    max_price=0
    max_name=''

    for name,price in products.items():
        if price>max_price:
            max_price=price
            max_name=name

    return max_name,max_price



def cheapest_product(products):
    min_price=0
    min_name=''

    for name,price in products.items():
        if price<min_price:
            min_price=price
            min_name=name

    return min_name,min_price


print('Total price:',total_price(products))
print('Most expensive:',most_expensive(products))
print('Cheapest product:',cheapest_product(products))