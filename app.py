import streamlit as st

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

st.title("UrbanDine - Food Ordering App")
st.subheader("Menu")

selected_items = []
total = 0

for item, price in menu.items():
    qty = st.number_input(f"{item} (₹{price})", min_value=0, step=1)
    if qty > 0:
        selected_items.append((item, qty, price))
        total += qty * price

coupon_code = st.text_input("Enter Coupon Code")

if st.button("Place Order"):
    st.write("### Order Summary:")
    for item, qty, price in selected_items:
        st.write(f"{qty} x {item} @ ₹{price} = ₹{qty * price}")
    
    discount = 0
    if coupon_code in coupons:
        discount = total * coupons[coupon_code]
        st.success(f"Coupon '{coupon_code}' applied! Discount: ₹{int(discount)}")
    elif coupon_code:
        st.error("Invalid coupon code.")
    
    st.write(f"*Total:* ₹{int(total - discount)}")
