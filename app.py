import streamlit as st

menu = {
    "Burger": 150,
    "Tacos": 100,
    "Fries": 80,
    "Iced Tea": 60,
    "Brownie": 70
}

st.title("Urban Dine - Food Ordering App")
st.subheader("Menu")

selected_items = []
subtotal = 0

# Item selection
for item, price in menu.items():
    qty = st.number_input(f"{item} (₹{price})", min_value=0, step=1, key=item)
    if qty > 0:
        selected_items.append((item, qty, price))
        subtotal += qty * price

# Place order
if st.button("Place Order"):
    if not selected_items:
        st.warning("Please select at least one item to place an order.")
    else:
        st.write("### 🧾 Order Summary:")
        for item, qty, price in selected_items:
            st.write(f"{qty} x {item} @ ₹{price} = ₹{qty * price}")
        
        st.write(f"### 💰 Total to Pay: ₹{subtotal}")
        st.success("✨ Thanks for ordering with us!")
