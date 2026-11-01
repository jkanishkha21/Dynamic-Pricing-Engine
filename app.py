import streamlit as st

st.title("Dynamic Pricing Engine")

st.write("Welcome to my Dynamic Pricing Engine!")

st.subheader("Product Demand Prediction")

st.write(
    "This application will help analyse product demand "
    "and support pricing decisions."
)

category = st.selectbox(
    "Select Product Category",
    ["Furniture", "Office Supplies", "Technology"]
)

st.write("Selected Category:", category)
