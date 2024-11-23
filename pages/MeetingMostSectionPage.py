from Controllers.MeetingMostSectionController import MeetingMostSectionController
import streamlit as st
import pandas as pd
import plotly.express as px



st.title("Meeting Most Section")


Controller = MeetingMostSectionController()
result = Controller.GET_MEETING_WITH_MOST_SECTION()


# Create DataFrame
data = pd.DataFrame(
    {
        "Total_Sections": [int(r["total_sections"]) for r
                  in result]
    },
    index=[f"MID: {r['mid']}" for r in result]
)

fig = px.bar(data, y="Total_Sections")
st.plotly_chart(fig)
