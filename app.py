# ============================================================
# 🚀 Grocery Store Target User Analyzer using NLP
# 🚀 Professional Streamlit app.py
# ============================================================

# ============================================================
# 📌 IMPORT LIBRARIES
# ============================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re
from wordcloud import WordCloud

# ============================================================
# 📌 PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Grocery Store NLP Analyzer",
    layout="wide"
)

# ============================================================
# 📌 TITLE
# ============================================================

st.title("🛒 Grocery Store Target User Analyzer using NLP")

st.markdown("""
This application analyzes grocery store management documents
using NLP techniques and extracts target users with
frequency analysis and visualizations.
""")

# ============================================================
# 📌 TEXT INPUT
# ============================================================

st.header("📄 Enter Grocery Store Document")

document_text = st.text_area(
    "Paste your grocery store management document here:",
    height=300
)

# ============================================================
# 📌 ANALYZE BUTTON
# ============================================================

if st.button("🚀 Analyze Document"):

    if document_text.strip() == "":
        st.warning("Please enter document text.")
    else:

        # ====================================================
        # 📌 CLEAN TEXT
        # ====================================================

        cleaned_text = re.sub(r'\s+', ' ', document_text)

        # ====================================================
        # 📌 USER TYPES
        # ====================================================

        user_types = [
            "Store Owner",
            "Store Manager",
            "Cashier",
            "Inventory Staff",
            "Suppliers",
            "Customers",
            "Admin"
        ]

        # ====================================================
        # 📌 FIND USERS
        # ====================================================

        found_users = []

        for user in user_types:

            matches = re.findall(
                re.escape(user),
                cleaned_text,
                re.IGNORECASE
            )

            found_users.extend(matches)

        # ====================================================
        # 📌 COUNT FREQUENCY
        # ====================================================

        user_counts = Counter(found_users)

        # ====================================================
        # 📌 DATAFRAME
        # ====================================================

        df = pd.DataFrame(
            user_counts.items(),
            columns=["User Type", "Frequency"]
        )

        # ====================================================
        # 📌 SHOW RESULTS
        # ====================================================

        st.header("📊 Analysis Results")

        st.dataframe(df)

        # ====================================================
        # 📌 CSV DOWNLOAD
        # ====================================================

        csv = df.to_csv(index=False)

        st.download_button(
            label="⬇ Download CSV Report",
            data=csv,
            file_name="target_user_analysis.csv",
            mime="text/csv"
        )

        # ====================================================
        # 📌 BAR CHART
        # ====================================================

        st.subheader("📈 Frequency Bar Chart")

        fig, ax = plt.subplots(figsize=(10, 5))

        ax.bar(df["User Type"], df["Frequency"])

        ax.set_xlabel("User Type")
        ax.set_ylabel("Frequency")
        ax.set_title("Target User Frequency Analysis")

        plt.xticks(rotation=20)

        st.pyplot(fig)

        # ====================================================
        # 📌 PIE CHART
        # ====================================================

        st.subheader("🥧 User Distribution")

        fig2, ax2 = plt.subplots(figsize=(7, 7))

        ax2.pie(
            df["Frequency"],
            labels=df["User Type"],
            autopct='%1.1f%%'
        )

        st.pyplot(fig2)

        # ====================================================
        # 📌 WORD CLOUD
        # ====================================================

        st.subheader("☁ WordCloud")

        wordcloud = WordCloud(
            width=1000,
            height=500,
            background_color='white'
        ).generate(cleaned_text)

        fig3, ax3 = plt.subplots(figsize=(14, 7))

        ax3.imshow(wordcloud, interpolation='bilinear')

        ax3.axis("off")

        st.pyplot(fig3)

        # ====================================================
        # 📌 SUCCESS MESSAGE
        # ====================================================

        st.success("✅ Analysis Completed Successfully!")

# ============================================================
# 📌 FOOTER
# ============================================================

st.markdown("---")

st.markdown(
    "Developed using Python, Streamlit, NLP, Pandas, and Matplotlib"
)
