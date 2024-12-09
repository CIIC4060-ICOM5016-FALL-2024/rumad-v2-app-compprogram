from Controllers.MostClassPerRoomController import MostClassPerRoomController
import streamlit as st
import plotly.express as px
import pandas as pd
from sidebar import make_sidebar
make_sidebar()

if "login_in" not in st.session_state:
    st.session_state.login_in = False

if(st.session_state.login_in == False):
    st.write("Please log in to see the data")

    if(st.button("Log in")):
        st.switch_page("Main_page.py")

else:

    st.title("Top 3 classes that where taught the most per room")


    try:
        rid = st.text_input("Insert RID")

        Controller = MostClassPerRoomController()
        isClicked = st.button("Send data") or rid


        if isClicked:
            # Create DataFrame
            result = Controller.GET_Most_Class_Per_Room(int(rid))
            data = pd.DataFrame(
                {
                    "Students": [r["students"] for r in result],
                    "Class_Info": [f"RID: {r['rid']}, Class Name: {r['class Name']}, Room:{r['room_number']}" for r in result]  # Creating a new column called room_info
                    #contains the rid and the room_number
                }
            )

            fig = px.bar(data, x="Class_Info", y="Students")
            st.plotly_chart(fig)
    except:
        try:
            int(rid)
            st.write("RID was not found")
        
        except:
            st.write("RID must be a number")


            