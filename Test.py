import streamlit as st

# Page Settings
st.set_page_config(
    page_title="Login Form",
    page_icon="🔐"
)

# Title
st.title("🔐 Login Form")

# Username & Password
username = st.text_input("Username")

password = st.text_input(
    "Password",
    type="password"
)

# Login Button
if st.button("Login"):

    if username == "admin" and password == "12345":
        st.success("✅ Login Successful")
        st.write("Welcome Admin")

    else:
        st.error("❌ Invalid Username or Password")