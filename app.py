import streamlit as st
import pandas as pd
import random
from sklearn.linear_model import LinearRegression
import numpy as np


st.title("Grocery Store Management Analysis")
st.write("Target User Frequency Analyzer")

def generate_data():
    items = ["Rice", "Milk", "Bread", "Eggs"]
    data = []

    for i in range(50):
        item = random.choice(items)
        qty = random.randint(1,5)
        price = random.randint(20,100)
        total = qty * price
        data.append([item, qty, price, total])

    return pd.DataFrame(data, columns=["Item","Qty","Price","Total"])

df = generate_data()

st.dataframe(df)

if st.button("Analyze"):
    st.write("Summary")
    st.write(df.describe())

    st.subheader(" AI Future Forecast")

df["Day"] = np.arange(len(df))

X = df[["Day"]]
y = df["Total"]

model = LinearRegression()
model.fit(X, y)

future_days = np.arange(len(df), len(df)+7).reshape(-1,1)
future_sales = model.predict(future_days)

forecast_df = pd.DataFrame({
    "Day": range(1,8),
    "Predicted Sales": future_sales
})
st.dataframe(forecast_df)

st.line_chart(forecast_df.set_index("Day"))

st.write("Top Selling Items")

st.bar_chart(df["Item"].value_counts())



