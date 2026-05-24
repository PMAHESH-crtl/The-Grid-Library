import streamlit as st
import pandas as pd
from datetime import datetime
import uuid

# PAGE CONFIG
st.set_page_config(page_title="THE GRID LIBRARY", layout="wide")

# LOAD CSS (Optional)
try:
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("style.css not found. Using default styling.")

# BUSINESS DETAILS
BUSINESS_NAME = "THE GRID LIBRARY"
PHONE = "7995966131"
EMAIL = "pakalamahesh08@gmail.com"

# PRODUCTS
products = [
    {
        "name": "Classic Wooden Frame",
        "category": "Standard",
        "price": 199,
        "image": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?auto=format&fit=crop&w=1200&q=80"
    },
    {
        "name": "Gallery Premium Frame",
        "category": "Gallery",
        "price": 299,
        "image": "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?auto=format&fit=crop&w=1200&q=80"
    },
    {
        "name": "Floating Glass Frame",
        "category": "Floating",
        "price": 399,
        "image": "https://images.unsplash.com/photo-1510076857177-7470076d4098?auto=format&fit=crop&w=1200&q=80"
    },
    {
        "name": "College Memory Frame",
        "category": "College",
        "price": 499,
        "image": "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&w=1200&q=80"
    }
]

# HEADER
st.markdown(
    f"""
    <div style="text-align:center;">
        <h1>{BUSINESS_NAME}</h1>
        <h4>
            Premium Photo Frames<br>
            📞 {PHONE} | 📧 {EMAIL}
        </h4>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# DISPLAY PRODUCTS
cols = st.columns(2)

for index, product in enumerate(products):

    with cols[index % 2]:

        st.image(product["image"], use_container_width=True)

        st.subheader(product["name"])
        st.write(f"Category: {product['category']}")
        st.markdown(
            f"<h3>₹ {product['price']}</h3>",
            unsafe_allow_html=True
        )

        # CUSTOMER DETAILS
        customer_name = st.text_input(
            "Customer Name",
            key=f"name_{index}"
        )

        customer_mobile = st.text_input(
            "Customer Mobile",
            key=f"mobile_{index}"
        )

        # PAYMENT BUTTON
        razorpay_link = "https://rzp.io/l/YOUR_PAYMENT_LINK"

        st.markdown(
            f"""
            <a href="{razorpay_link}" target="_blank">
                <button style="
                    background:black;
                    color:white;
                    padding:12px;
                    width:100%;
                    border:none;
                    border-radius:10px;
                    cursor:pointer;
                    font-size:18px;
                ">
                    Buy Now
                </button>
            </a>
            """,
            unsafe_allow_html=True
        )

        # PAYMENT ID INPUT
        transaction_id = st.text_input(
            "Enter Razorpay Payment ID",
            key=f"txn_{index}"
        )

        # GENERATE RECEIPT
        if st.button(
            f"Generate Receipt - {product['name']}",
            key=f"receipt_{index}"
        ):

            if not customer_name or not customer_mobile or not transaction_id:
                st.error("Please fill all details before generating receipt.")
            else:
                order_id = str(uuid.uuid4())[:8]

                receipt = {
                    "Order ID": order_id,
                    "Customer": customer_name,
                    "Mobile": customer_mobile,
                    "Transaction ID": transaction_id,
                    "Product": product["name"],
                    "Amount": product["price"],
                    "Seller": "PAKALA MAHESH",
                    "Seller Mobile": PHONE,
                    "Time": str(datetime.now())
                }

                df = pd.DataFrame([receipt])

                st.success("Payment Receipt Generated Successfully")

                st.dataframe(df)

                csv = df.to_csv(index=False)

                st.download_button(
                    label="Download Receipt",
                    data=csv,
                    file_name=f"{order_id}.csv",
                    mime="text/csv"
                )

        st.divider()
