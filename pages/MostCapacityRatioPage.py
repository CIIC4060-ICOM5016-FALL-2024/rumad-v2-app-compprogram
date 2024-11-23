from Controllers.MostCapacityRatioController import MostCapacityRatioController
import streamlit as st
import pandas as pd 
import plotly_express as px



st.title("Most Capacity Ratio")
try:
    rid = st.text_input("Insert RID")


    Controller = MostCapacityRatioController()
    result = Controller.GET_MOST_CAPACITY_RATIO(rid)
    isClicked = st.button("Send data")

    if isClicked:
        # Create DataFrame
        data = pd.DataFrame(
            {
                "student_to_capacity_ratio": [r["student_to_capacity_ratio"] for r in result],
                "room_info": [f"RID: {r['rid']}, Room: {r['room_number']}" for r in result]  # Creating a new column called room_info
                #contains the rid and the room_number
            }
        )


        fig = px.bar(data, y="student_to_capacity_ratio")
        st.plotly_chart(fig)
except:
    try:
        int(rid)
        st.write("Rid was not found")
    
    except:
        st.write("Rid must be a number")
