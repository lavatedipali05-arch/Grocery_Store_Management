import streamlit as st
import pandas as pd
import random

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

    st.write("Top Selling Items")
    st.bar_chart(df["Item"].value_counts())
