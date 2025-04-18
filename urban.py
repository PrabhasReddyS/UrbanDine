menu = {
    'Burger': 150,
    'Tacos': 100,
    'Fries': 80,
    'Iced Tea': 60,
    'Brownie': 70
}

# 🔥 Added DINE20 coupon

print("🍔 Welcome to Urban Dine!\nHere's our menu:")
for item in menu:
    print(f"{item}: {menu[item]} Rs")

orders = {}

# 🛒 Ordering loop
while True:
    item = input("\nEnter item to order: ").title()
    if item in menu:
        qty = int(input(f"How many {item}s? "))
        if item in orders:
            orders[item] += qty
        else:
            orders[item] = qty
    else:
        print("❌ Item not on the menu.")
    
    if input("Order more? (y/n): ").lower() != 'y':
        break

# 🧾 Show receipt
if not orders:
    print("\n❌ No items ordered.")
else:
    print("\n🧾 Order Summary:")
    subtotal = 0
    for item, qty in orders.items():
        price = menu[item]
        total_price = price * qty
        subtotal += total_price
        print(f"{qty} x {item} @ {price} Rs = {total_price} Rs")

   
    grand_total = subtotal 
    print(f"\n💵 Subtotal: {subtotal} Rs")
    print(f"🎉 Total to Pay: {int(grand_total)} Rs")
    print("\n✨ Thanks for ordering with us!")
