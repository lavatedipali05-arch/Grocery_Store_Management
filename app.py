import streamlit as st
import pandas as pd

st.title("Grocery Store Management Analysis")

df = pd.read_csv("dataset.csv")

df.columns = df.columns.str.strip()

st.subheader("Dataset Preview")
st.dataframe(df)

st.subheader("Filter Data")

city = st.selectbox("Select City", df["City"].unique())
gender = st.selectbox("Select Gender", df["Gender"].unique())

filtered_df = df[(df["City"] == city) & (df["Gender"] == gender)]

st.write("Filtered Data")
st.dataframe(filtered_df)

st.subheader("Sales Analysis")


city_sales = df.groupby("City")["Total"].sum()
st.write("Total Sales by City")
st.bar_chart(city_sales)

product_sales = df.groupby("Product line")["Total"].sum()
st.write("Sales by Product Line")
st.bar_chart(product_sales)


st.subheader("Key Metrics")

total_sales = df["Total"].sum()
avg_rating = df["Rating"].mean()

st.write("Total Sales:", total_sales)
st.write("Average Rating:", round(avg_rating, 2))
