from Controllers.MostPrerequisiteController import MostPrerequisiteController
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

    st.title("Top 3 classes that appears the most as prerequisite to other classes")


    Controller = MostPrerequisiteController()
    result = Controller.GET_TOP_PREREQUISITE()


    # Create DataFrame
    data = pd.DataFrame(
        {
            "Total": [int(r["total"]) for r
                    in result],
        },
        index=[f"Reqid: {r['requid']}, {r['cdesc']}" for r in result]
    )


    fig = px.bar(data, y="Total")
    st.plotly_chart(fig)