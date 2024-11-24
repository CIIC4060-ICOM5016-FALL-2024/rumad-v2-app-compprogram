from Controllers.MostCapacityRoomsController import MostCapacityRoomsController
import streamlit as st
import plotly.express as px
import pandas as pd
st.title("Top 3 rooms with the most capacity")


Controller = MostCapacityRoomsController()
building = st.selectbox("Choose a building", ["Monzon","Stefani","Software"])#Create the drop down list for the possible ansewers

result = Controller.GET_Most_Capacity_Rooms(building)
    
data = pd.DataFrame(
    {
        "Capacity": [r["capacity"] for r in result],
        "bulding_info": [f"RID: {r['rid']}, Building: {r['building']}, Room: {r['room_number']}" for r in result]  # Creating a new column called room_info
        #contains the rid and the room_number
    }
)


fig = px.bar(data, x="bulding_info", y="Capacity")
st.plotly_chart(fig)
