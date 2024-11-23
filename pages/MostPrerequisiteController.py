from Controllers.MostPrerequisiteController import MostPrerequisiteController
import streamlit as st
import pandas as pd
import plotly.express as px


st.title("Least Class Taught")


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