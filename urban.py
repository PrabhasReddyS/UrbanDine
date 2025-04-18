menu = {
    'Burger': 150,
    'Tacos': 100,
    'Fries': 80,
    'Iced Tea': 60,
    'Brownie': 70
}

print("🍔 Welcome to Urban Dine!\nHere's our menu:")
for item, price in menu.items():
    print(f"{item}: {price} Rs")

orders = {}

# Ordering loop
while True:
    item = input("\nEnter item to order: ").title()
    if item in menu:
        qty = int(input(f"How many {item}s? "))
        orders[item] = orders.get(item, 0) + qty
    else:
        print("❌ Item not on the menu.")
    
    if input("Order more? (y/n): ").lower() != 'y':
        break

# Summary
if not orders:
    print("\n❌ No items ordered.")
else:
    print("\n🧾 Order Summary:")
    total = 0
    for item, qty in orders.items():
        price = menu[item]
        cost = price * qty
        print(f"{qty} x {item} @ {price} Rs = {cost} Rs")
        total += cost

    print(f"\n💰 Total to Pay: {total} Rs")
    print("✨ Thanks for ordering with us!")
