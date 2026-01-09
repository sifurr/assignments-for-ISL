raw_inventory = ["Laptop:1000", "Mouse:25", "Monitor:300", "Keyboard:50"]


def analyze_inventory(products):
    extracted_products = [(product.split(":")[0], int(product.split(":")[1])) for product in products]

    return extracted_products


products = analyze_inventory(raw_inventory)
most_expensive_product_price = max([x[1] for x in products])
cheapest_product_price = min([x[1] for x in products])

print(f"Analyzed Inventory: {products}")
print(f"Most expensive item price: {most_expensive_product_price}")
print(f"Cheapest item price: {cheapest_product_price}")