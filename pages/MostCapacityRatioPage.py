from Controllers.MostCapacityRatioController import MostCapacityRatioController
import streamlit as st
import pandas as pd 
import plotly_express as px
from sidebar import make_sidebar
make_sidebar()

if "login_in" not in st.session_state:
    st.session_state.login_in = False

if(st.session_state.login_in == False):
    st.write("Please log in to see the data")

    if(st.button("Log in")):
        st.switch_page("Main_page.py")

else:

    st.title("Top 3 sections with the most student-to-capacity ratio")
    
    try:
        rid = st.text_input("Insert RID")


        Controller = MostCapacityRatioController()
        result = Controller.GET_MOST_CAPACITY_RATIO(rid)
        isClicked = st.button("Send data") or rid

        if isClicked:
            # Create DataFrame
            data = pd.DataFrame(
                {
                    "student_to_capacity_ratio": [r["student_to_capacity_ratio"] for r in result],
                    "room_info": [f"RID: {r['rid']}, Room: {r['room_number']}, SID: {r['sid']}" for r in result]  # Creating a new column called room_info
                    #contains the rid and the room_number
                }
            )


            fig = px.bar(data, x="room_info", y="student_to_capacity_ratio")
            st.plotly_chart(fig)
    except:
        try:
            int(rid)
            st.write("Rid was not found")
        
        except:
            st.write("Rid must be a number")
