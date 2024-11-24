from Controllers.MostClassPerRoomController import MostClassPerRoomController
import streamlit as st
import plotly.express as px
import pandas as pd
st.title("Top 3 classes that where taught the most per room")


try:
    rid = int(st.text_input("Insert CID"))

    Controller = MostClassPerRoomController()
    result = Controller.GET_Most_Class_Per_Room(rid)
    isClicked = st.button("Send data") or rid


    if isClicked:
        # Create DataFrame
        data = pd.DataFrame(
            {
                "Students": [r["students"] for r in result],
                "Class_Info": [f"CID: {r['cid']}, Class Name: {r['class Name']}, Room:{r['room_number']}" for r in result]  # Creating a new column called room_info
                #contains the rid and the room_number
            }
        )

        fig = px.bar(data, x="Class_Info", y="Students")
        st.plotly_chart(fig)
except:
    try:
        int(rid)
        st.write("Cid was not found")
    
    except:
        st.write("Cid must be a number")


        