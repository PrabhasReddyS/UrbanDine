import streamlit as st

# Menu and coupons
menu = {
    "Pizza": 250,
    "Burger": 150,
    "Pasta": 200,
    "Fries": 100
}

coupons = {
    "URBAN10": 0.10,
    "DINE20": 0.20
}

# Title and subheader
st.title("UrbanDine - Food Ordering App")
st.subheader("Menu")

# Order logic
selected_items = []
subtotal = 0

# Show menu and get quantities
for item, price in menu.items():
    qty = st.number_input(f"{item} (₹{price})", min_value=0, step=1, key=item)
    if qty > 0:
        selected_items.append((item, qty, price))
        subtotal += qty * price

# ✅ This input is ALWAYS visible before the button
coupon_code = st.text_input("Enter Coupon Code").strip().upper()

# Place Order button
if st.button("Place Order"):
    if not selected_items:
        st.warning("Please select at least one item to place an order.")
    else:
        st.write("### 🧾 Order Summary:")
        for item, qty, price in selected_items:
            st.write(f"{qty} x {item} @ ₹{price} = ₹{qty * price}")
        
        # Apply coupon
        discount = 0
        if coupon_code:
            if coupon_code in coupons:
                discount = subtotal * coupons[coupon_code]
                st.success(f"Coupon '{coupon_code}' applied! Discount: ₹{int(discount)}")
            else:
                st.error("Invalid coupon code.")

        total = subtotal - discount

        # Final bill
        st.write(f"**Subtotal:** ₹{int(subtotal)}")
        st.write(f"**Discount:** ₹{int(discount)}")
        st.write(f"### ✅ Total to Pay: ₹{int(total)}")
