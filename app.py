import streamlit as st
import pandas as pd
import re
from collections import Counter
import matplotlib.pyplot as plt

st.title("Grocery Store Management Analysis")

st.write("Target User Frequency Analyzer")

text = st.text_area(
    "Enter Grocery Store Document",
    height=250
)

if st.button("Analyze"):

    if text == "":
        st.warning("Please enter some text")

    else:

        cleaned_text = re.sub(r"\s+", " ", text)

        users = [
            "Store Owner",
            "Store Manager",
            "Cashier",
            "Inventory Staff",
            "Customers",
            "Suppliers",
            "Admin"
        ]

        found = []

        for user in users:

            data = re.findall(
                user,
                cleaned_text,
                re.IGNORECASE
            )

            found.extend(data)

        counts = Counter(found)

        df = pd.DataFrame(
            counts.items(),
            columns=["User Type", "Count"]
        df =pd.read_cvs("SuperMarket dataset.cvs")

        st.subheader("Analysis Result")

        st.dataframe(df)

        csv = df.to_csv(index=False)

        st.download_button(
            "Download CSV",
            csv,
            "report.csv",
            "text/csv"
        )

        fig, ax = plt.subplots()

        ax.bar(
            df["User Type"],
            df["Count"]
        )

        plt.xticks(rotation=15)

        plt.xlabel("User Type")
        plt.ylabel("Count")

        plt.title("Target User Analysis")

        st.pyplot(fig)

        st.success("Analysis Completed")
