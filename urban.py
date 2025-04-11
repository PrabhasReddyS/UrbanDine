menu = {
    'Burger': 150,
    'Tacos': 100,
    'Fries': 80,
    'Iced Tea': 60,
    'Brownie': 70
}

coupons = {'URBAN10': 0.10}

print("🍔 Welcome to Urban Dine!\nHere's our menu:")
for item in menu:
    print(f"{item}: {menu[item]} Rs")

orders = []
while True:
    item = input("\nEnter item to order: ").title()
    if item in menu:
        orders.append(item)
    else:
        print("Item not on the menu.")
    if input("Order more? (y/n): ").lower() != 'y':
        break

if not orders:
    print("❌ No items ordered.")
else:
    total = sum(menu[i] for i in orders)
    coupon = input("Have a coupon? (press Enter to skip): ").upper()
    if coupon in coupons:
        total *= (1 - coupons[coupon])
        print(f"✅ Coupon applied! New total: {total:.2f} Rs")
    else:
        print(f"Total: {total:.2f} Rs")

print("✨ Thanks for ordering with us!")