import streamlit as st
import joblib

model = joblib.load("fraud_model.pkl")

st.title("🚚 Online Delivery Fraud Detection") 

order_amount = st.number_input("Order Amount (₹)", 100, 10000, 500)
payment_mode = st.selectbox("Payment Mode", ["Online", "COD"]) 
delivery_attempts = st.slider("Delivery Attempts", 1, 5, 1)
previous_orders = st.slider("Previous Orders", 0, 50, 5)
cancel_rate = st.slider("Cancel Rate", 0.0, 1.0, 0.2)

payment_encoded = 1 if payment_mode == "Online" else 0 

if st.button("Check Fraud"):
    input_data = [[
        order_amount,
        payment_encoded,
        delivery_attempts, 
        previous_orders,
        cancel_rate
    ]]
     
    result = model.predict(input_data)

    if result[0] == 1:
        st.error("🚨 Fraudulent Order Detected")
    else:
        st.success("✅ Order is Genuine")
