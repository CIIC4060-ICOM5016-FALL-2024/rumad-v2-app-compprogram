import streamlit as st
from Controllers.LoginController import LoginController
import requests as rq

# App title and header
st.title("Welcome to the new Putty!")
st.header("Before you continue, please make sure you have an account")

# User inputs
username = st.text_input("Enter username")
password = st.text_input("Enter password", type="password")

# Button to trigger login
if st.button("Login"):
    if username and password:  # Check if inputs are filled
        Controller = LoginController()
        Allowed = Controller.Verification(username, password)
        

        try:
            # Make API request after successful verification
            response = Allowed
            if response == 200:
                st.success("Login successful!")
        except:
            st.error(f"Failed to fetch data with username: {username} and password: {password}")
            
st.write()