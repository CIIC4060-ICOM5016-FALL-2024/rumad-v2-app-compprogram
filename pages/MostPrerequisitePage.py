from Controllers.MostPrerequisiteController import MostPrerequisiteController
import streamlit as st
import pandas as pd
import plotly.express as px


if(st.session_state.login_in == False):
    st.write("Go back to the Main page and logged in, if you want to see the data")

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