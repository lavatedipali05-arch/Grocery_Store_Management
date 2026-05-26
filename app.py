import streamlit as st
import pandas as pd

st.title("Grocery Store App")

# load files
df1 = pd.read_csv("dataset.csv")
df2 = pd.read_csv("target_user_analysis.csv")

# clean column names
df1.columns = df1.columns.str.strip().str.lower()
df2.columns = df2.columns.str.strip().str.lower()

# 🔍 check columns (important)
st.write("Columns df1:", df1.columns)

# -------------------
# Sales Data
# -------------------
st.header("Sales Data")
st.write(df1.head())

# 🔥 use lowercase 'total'
city_sales = df1.groupby("city")["total"].sum()
st.bar_chart(city_sales)

# -------------------
# User Data
# -------------------
st.header("User Data")
st.write(df2.head())

gender = df2["gender"].value_counts()
st.bar_chart(gender)
