import streamlit as st
import pandas as pd

st.set_page_config(page_title="ADMIN DASHBOARD")

st.title("THE GRID LIBRARY - ADMIN")

st.subheader("Upload New Frames")

name = st.text_input("Frame Name")

category = st.selectbox(
    "Category",
    ["Standard", "Gallery", "Floating", "College"]
)

price = st.number_input("Price", min_value=199)

image = st.text_input("Image URL")

if st.button("Upload Frame"):

    new_data = {
        "Name": name,
        "Category": category,
        "Price": price,
        "Image": image
    }

    df = pd.DataFrame([new_data])

    try:
        old = pd.read_csv("frames.csv")
        df = pd.concat([old, df])
    except:
        pass

    df.to_csv("frames.csv", index=False)

    st.success("Frame Uploaded Successfully")

try:
    data = pd.read_csv("frames.csv")
    st.dataframe(data)
except:
    st.warning("No Frames Uploaded Yet")
