import streamlit as st
from Controllers.LoginController import LoginController

st.title("Welcome to the new Putty!!\n")
st.header("Before you continue, please make sure you have an account")

username = st.text_input("Enter username")
password = st.text_input("Enter password")

Controller = LoginController()
Allowed = Controller.Verification(username,password)

if(Allowed):
    st.write("Yuppy it works")
