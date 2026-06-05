import streamlit as st
import pandas as pd
import random
import numpy as np
from sklearn.linear_model import LinearRegression
from io import BytesIO
from reportlab.pdfgen import canvas


USERNAME = "admin"
PASSWORD = "admin123"

st.sidebar.title("Admin Login")

user = st.sidebar.text_input("Username")
pwd = st.sidebar.text_input("Password", type="password")

if user != USERNAME or pwd != PASSWORD:
    st.warning("Please Login First")
    st.stop()


st.title("Grocery Store Management Analysis")
st.write("AI Powered Grocery Analytics Dashboard")


def generate_data():
    items = ["Rice", "Milk", "Bread", "Eggs"]

    customers = [
        "Rahul",
        "Amit",
        "Priya",
        "Sneha",
        "Rohit"
    ]

    data = []

    for i in range(50):
        customer = random.choice(customers)
        item = random.choice(items)
        qty = random.randint(1, 5)
        price = random.randint(20, 100)
        expiry_days = random.randint(1,30)

        total = qty * price

        data.append([
            customer,
            item,
            qty,
            price,
            total
            expiry_days
        ])

    return pd.DataFrame(
        data,
        columns=[
            "Customer",
            "Item",
            "Qty",
            "Price",
            "Total"
            "Expiry_Days"
        ]
    )

df = generate_data()


sales_count = df["Item"].value_counts()

for item in sales_count.index:
    if sales_count[item] > 12:
        df.loc[df["Item"] == item, "Price"] *= 1.10

df["Total"] = df["Qty"] * df["Price"]


st.subheader(" Business KPIs")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Sales",
    f"₹{int(df['Total'].sum())}"
)

col2.metric(
    "Orders",
    len(df)
)

col3.metric(
    "Products",
    df["Item"].nunique()
)


st.subheader("Sales Records")
st.dataframe(df)

st.subheader("Sales Recoreds")
st.dataframe(df)


st.subheader("Smart Expiry Alert System")

expiring_products = df[df["Expiry_Days"] <= 7]

if not expiring_products.empty:
    st.warning("Products Expiring Within 7 Days")
    st.dataframe(expiring_products)

urgent = df[df["Expiry_Days"] <= 3]

if not urgent.empty:
    st.error(" Urgent: Products Expiring Within 3 Days")
    st.dataframe(urgent)

discount_df = df[df["Expiry_Days"] <= 5]

if not discount_df.empty:
    st.info("Suggested Action: Offer 20% discount on products nearing expiry.")

st.subheader("Low Stock Alert")

low_stock = df[df["Qty"] <= 2]

if not low_stock.empty:
    st.error("Low Stock Products Found")
    st.dataframe(low_stock)


if st.button("Analyze Data"):

    st.subheader("Summary Statistics")
    st.write(df.describe())

st.subheader(" AI Sales Forecast")

df["Day"] = np.arange(len(df))

X = df[["Day"]]
y = df["Total"]

model = LinearRegression()
model.fit(X, y)

future_days = np.arange(
    len(df),
    len(df) + 7
).reshape(-1, 1)

future_sales = model.predict(future_days)

forecast_df = pd.DataFrame({
    "Day": range(1, 8),
    "Predicted Sales": future_sales
})

st.dataframe(forecast_df)

st.line_chart(
    forecast_df.set_index("Day")
)


st.subheader(" Top Selling Items")

st.bar_chart(
    df["Item"].value_counts()
)

st.subheader("Customer Loyalty Score")

loyalty = (
    df.groupby("Customer")
    .size()
    .reset_index(name="Orders")
)

st.dataframe(loyalty)


st.subheader(" Smart Product Recommendation")

top_item = (
    df["Item"]
    .value_counts()
    .idxmax()
)

recommend = {
    "Rice": "Milk",
    "Milk": "Bread",
    "Bread": "Eggs",
    "Eggs": "Rice"
}

st.success(
    f"Customers buying {top_item} also buy {recommend[top_item]}"
)


st.subheader("Waste Reduction Analytics")

df["Unsold"] = 10 - df["Qty"]

waste = (
    df.groupby("Item")["Unsold"]
    .sum()
)

st.bar_chart(waste)


pdf_buffer = BytesIO()

c = canvas.Canvas(pdf_buffer)

c.drawString(
    100,
    750,
    "Grocery Store Sales Report"
)

c.drawString(
    100,
    730,
    f"Total Records: {len(df)}"
)

c.drawString(
    100,
    710,
    f"Total Sales: ₹{int(df['Total'].sum())}"
)

c.save()

pdf_buffer.seek(0)

st.download_button(
    label=" Download PDF Report",
    data=pdf_buffer,
    file_name="sales_report.pdf",
    mime="application/pdf"
)

st.success(
    "Project Loaded Successfully"
)
