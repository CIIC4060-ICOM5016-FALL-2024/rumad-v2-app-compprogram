from Controllers.MeetingMostSectionController import MeetingMostSectionController
import streamlit as st
import pandas as pd
import plotly.express as px
from sidebar import make_sidebar
make_sidebar()

if(st.session_state.login_in == False):
    st.write("Please log in to see the data")

    if(st.button("Log in")):
        st.switch_page("Main_page.py")

else:

    st.title("Top 5 meetings with the most sections")


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
