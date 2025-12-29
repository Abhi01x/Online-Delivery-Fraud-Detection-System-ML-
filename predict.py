import joblib

model = joblib.load("fraud_model.pkl") 

# Sample order
sample_order = [[2000, 0, 3, 2, 0.6]]  # COD, high risk

prediction = model.predict(sample_order)

if prediction[0] == 1:
    print("🚨 Fraudulent Order Detected")
else:
    print("✅ Genuine Order")
