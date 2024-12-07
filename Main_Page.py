from main import *
import pandas as pd
import streamlit as st
from Controllers.LoginController import LoginController
import requests as rq
from sidebar import make_sidebar


if "login_in" not in st.session_state:
    st.session_state.login_in = False

make_sidebar()

# App title and header

if(st.session_state.login_in == False):
    st.title("Welcome to the new Putty!")
    if st.session_state.login_in == False:
        st.header("Before you continue, please make sure you have an account")

        # User inputs
        username = st.text_input("Enter username")
        password = st.text_input("Enter password", type="password")

        # Button to trigger login
        if(st.button("Create Accout")):
            Controller = LoginController()
            CreateAccount = Controller.CreateAccount(username,password)
            if(CreateAccount == 201):
                st.write("Created succesfully")
            else:
                st.write("Try another username")
        if st.button("Login"):
            if username and password:  # Check if inputs are filled
                Controller = LoginController()
                Allowed = Controller.Verification(username, password)
                try:
                    # Make API request after successful verification
                    response = Allowed
                    if response == 200:
                        st.success("Login successful!")
                        st.session_state.login_in = True    
                    else:
                        raise # this error is to force the except
                except:
                    st.error(f"Failed to fetch data with username: {username} and password: {password}")
                    st.session_state.login_in = False
            elif(username):
                st.error("Write a password")
            else:
                st.error("Write a username")

    if (st.session_state.login_in == True):
        st.rerun()

# --------------------------------------------------------------------------------------------------------------------------------
if(st.session_state.login_in == True):
    st.title("Welcome to the new Putty!")
    page = st.selectbox("Choose a page", ["Home", "All Classes", "All Rooms","All Sections","All Meetings","All Requisites"])
    st.session_state.page = page

    if st.session_state.page == "Home":
        # Render home page content
        st.write("In the side bar, you can see all the different options for all the local and Global Statistics")
        st.write("Also, in the current Drop Down list you can verify all the information of all the tables")
    elif st.session_state.page == "All Classes":
        Controller = ClassController()
        result = Controller.GetAllClasses()
        order_result = pd.DataFrame(result)
        st.dataframe(order_result,use_container_width=True)
    elif st.session_state.page == "All Rooms":
        Controller = RoomController()
        result = Controller.GetAllRooms()
        order_result = pd.DataFrame(result)
        st.dataframe(order_result,use_container_width=True)
    elif st.session_state.page == "All Sections":
        Controller = SectionController()
        result = Controller.GetAllSections()
        order_result = pd.DataFrame(result)
        st.dataframe(order_result,use_container_width=True)
    elif st.session_state.page == "All Meetings":
        Controller = MeetingController()
        result = Controller.GetAllMeetings()
        order_result = pd.DataFrame(result)
        st.dataframe(order_result,use_container_width=True)
    elif st.session_state.page == "All Requisites":
        Controller = RequisiteController()
        result = Controller.GetAllRequisites()
        order_result = pd.DataFrame(result)
        st.dataframe(order_result,use_container_width=True)
        