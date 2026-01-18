menu = { "Espresso": 3.50, "Latte": 4.50, "Gold_Flake_Coffee": 50.00, "Sandwich": 8.00, "Luxury_Truffle": 25.00 }

print("===== Menu Before The Update =====")
for name, price in menu.items():
    print(f"{name}: ${price}")

print("\n===== Menu After The Update =====")
for name in list(menu.keys()):
    if menu[name] > 10:
        del menu[name]

for name, price in menu.items():
    print(f"{name}: ${price}")



