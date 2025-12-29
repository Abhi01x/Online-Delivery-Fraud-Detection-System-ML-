import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def load_data():
    df = pd.read_csv("data/orders.csv")

    le = LabelEncoder()
    df["payment_mode"] = le.fit_transform(df["payment_mode"])

    X = df.drop("is_fraud", axis=1)
    y = df["is_fraud"] 

    return train_test_split(X, y, test_size=0.2, random_state=42)
