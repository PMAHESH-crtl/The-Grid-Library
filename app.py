import streamlit as st
import pandas as pd
from PIL import Image
import os
from datetime import datetime

st.set_page_config(page_title="THE GRID LIBRARY", layout="wide")

# -----------------------------
# BUSINESS DETAILS
# -----------------------------

BUSINESS_NAME = "THE GRID LIBRARY"
PHONE = "7995966131"
EMAIL = "pakalamahesh08@gmail.com"
UPI_ID = "7995966131@ptsbi"

# -----------------------------
# PRODUCTS
# -----------------------------

products = [
    {
        "name": "Classic Wooden Frame",
        "category": "Standard",
        "price": 199,
        "image": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?auto=format&fit=crop&w=1200&q=80"
    },
    {
        "name": "Modern Gallery Frame",
        "category": "Gallery",
        "price": 199,
        "image": "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?auto=format&fit=crop&w=1200&q=80"
    },
    {
        "name": "Floating Glass Frame",
        "category": "Floating",
        "price": 199,
        "image": "https://images.unsplash.com/photo-1510076857177-7470076d4098?auto=format&fit=crop&w=1200&q=80"
    },
    {
        "name": "College Memory Frame",
        "category": "College",
        "price": 199,
        "image": "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&w=1200&q=80"
    }
]

# -----------------------------
# HEADER
# -----------------------------

st.title(BUSINESS_NAME)
st.subheader("Premium Photo Frames")

st.write(f"📞 {PHONE}")
st.write(f"📧 {EMAIL}")
st.write(f"💳 UPI: {UPI_ID}")

st.divider()

# -----------------------------
# PRODUCTS
# -----------------------------

cols = st.columns(2)

for index, product in enumerate(products):

    with cols[index % 2]:

        st.image(product["image"])

        st.subheader(product["name"])

        st.write(f"Category: {product['category']}")
        st.write(f"Price: ₹{product['price']}")

        if st.button(f"Buy {product['name']}"):

            st.success("Order Added Successfully")

            st.image(
                "https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=upi://pay?pa=7995966131@ptsbi",
                width=300
            )

            st.subheader("Scan & Pay")

            customer_name = st.text_input(
                "Customer Name",
                key=f"name_{index}"
            )

            payment_id = st.text_input(
                "Transaction ID",
                key=f"payment_{index}"
            )

            if st.button(
                f"Generate Receipt {product['name']}",
                key=f"receipt_{index}"
            ):

                receipt = {
                    "Customer": customer_name,
                    "Transaction ID": payment_id,
                    "Product": product["name"],
                    "Amount": product["price"],
                    "Seller": "PAKALA MAHESH",
                    "Seller Mobile": PHONE,
                    "Time": str(datetime.now())
                }

                df = pd.DataFrame([receipt])

                receipt_file = f"receipt_{index}.csv"

                df.to_csv(receipt_file, index=False)

                st.success("Receipt Generated Successfully")

                st.dataframe(df)

                with open(receipt_file, "rb") as file:
                    st.download_button(
                        "Download Receipt",
                        file,
                        file_name=receipt_file
                    )
