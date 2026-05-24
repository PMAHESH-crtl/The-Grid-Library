import streamlit as st
import pandas as pd
from datetime import datetime
import uuid

st.set_page_config(
    page_title="THE GRID LIBRARY",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM STYLING
# ---------------------------------------------------

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
    background-color: #0f0f0f;
    color: white;
}

.main-title {
    text-align: center;
    font-size: 65px;
    font-weight: bold;
    color: #d4af37;
    margin-top: 20px;
}

.sub-title {
    text-align: center;
    font-size: 20px;
    color: #d9d9d9;
    margin-bottom: 40px;
}

.product-card {
    background: linear-gradient(145deg, #1c1c1c, #121212);
    padding: 20px;
    border-radius: 25px;
    box-shadow: 0px 8px 25px rgba(212,175,55,0.2);
    margin-bottom: 30px;
    transition: 0.3s;
}

.product-card:hover {
    transform: scale(1.02);
}

.product-image img {
    border-radius: 20px;
}

.price {
    font-size: 30px;
    font-weight: bold;
    color: #d4af37;
    margin-top: 10px;
}

.buy-btn {
    background: #d4af37;
    color: black;
    padding: 14px;
    border-radius: 12px;
    text-align: center;
    font-size: 18px;
    font-weight: bold;
    text-decoration: none;
    display: block;
    margin-top: 15px;
}

.buy-btn:hover {
    background: white;
}

.receipt-box {
    background: #1a1a1a;
    padding: 20px;
    border-radius: 20px;
    border: 1px solid #d4af37;
}

footer {
    text-align:center;
    margin-top:40px;
    color:gray;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# BUSINESS DETAILS
# ---------------------------------------------------

BUSINESS_NAME = "THE GRID LIBRARY"
PHONE = "7995966131"
EMAIL = "pakalamahesh08@gmail.com"

# ---------------------------------------------------
# PRODUCTS
# ---------------------------------------------------

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

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown(
    f"""
    <div class='main-title'>
        {BUSINESS_NAME}
    </div>

    <div class='sub-title'>
        Premium Luxury Photo Frames <br><br>
        📞 {PHONE} &nbsp;&nbsp;&nbsp;
        📧 {EMAIL}
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------
# PRODUCTS DISPLAY
# ---------------------------------------------------

cols = st.columns(2)

for index, product in enumerate(products):

    with cols[index % 2]:

        st.markdown("<div class='product-card'>", unsafe_allow_html=True)

        st.markdown("<div class='product-image'>", unsafe_allow_html=True)

        st.image(product["image"])

        st.markdown("</div>", unsafe_allow_html=True)

        st.subheader(product["name"])

        st.write(f"Category: {product['category']}")

        st.markdown(
            f"<div class='price'>₹ {product['price']}</div>",
            unsafe_allow_html=True
        )

        customer_name = st.text_input(
            "Customer Name",
            key=f"name_{index}"
        )

        customer_mobile = st.text_input(
            "Customer Mobile",
            key=f"mobile_{index}"
        )

        # REPLACE WITH YOUR REAL RAZORPAY LINK
        razorpay_link = "https://rzp.io/l/YOUR_PAYMENT_LINK"

        st.markdown(
            f"""
            <a href="{razorpay_link}" target="_blank">
                <div class='buy-btn'>
                    Buy Now
                </div>
            </a>
            """,
            unsafe_allow_html=True
        )

        transaction_id = st.text_input(
            "Enter Razorpay Payment ID",
            key=f"txn_{index}"
        )

        if st.button(
            f"Generate Receipt",
            key=f"receipt_{index}"
        ):

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
                "Date": str(datetime.now())
            }

            df = pd.DataFrame([receipt])

            st.success("Payment Receipt Generated Successfully")

            st.markdown(
                "<div class='receipt-box'>",
                unsafe_allow_html=True
            )

            st.dataframe(df)

            st.markdown("</div>", unsafe_allow_html=True)

            csv = df.to_csv(index=False)

            st.download_button(
                "Download Receipt",
                csv,
                file_name=f"{order_id}.csv",
                mime="text/csv"
            )

        st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("""
<footer>
© 2026 THE GRID LIBRARY • All Rights Reserved
</footer>
""", unsafe_allow_html=True)
