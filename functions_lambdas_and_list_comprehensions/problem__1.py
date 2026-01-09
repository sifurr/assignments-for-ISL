prices = [100, 250, 400, 50]


def calculate_discount(product_prices, discount):
    percentage = discount / 100
    discounted_price = [(price - price * percentage) for price in product_prices]
    
    return discounted_price


print("Product Prices (before discount):", prices)
discount = int(input("Enter the discount in percent: "))
reduced_price = calculate_discount(prices, discount)
print("Product Prices (after discount):")
print(reduced_price)
