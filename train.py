from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
from preprocess import load_data

X_train, X_test, y_train, y_test = load_data()

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

joblib.dump(model, "fraud_model.pkl")

print(f"Model Accuracy: {accuracy * 100:.2f}%")
