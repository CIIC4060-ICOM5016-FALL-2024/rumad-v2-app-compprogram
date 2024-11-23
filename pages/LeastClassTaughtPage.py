from Controllers.LeastClassTaughtController import LeastClassTaughtController
import streamlit as st
import pandas as pd
import plotly.express as px


st.title("Least Class Taught")


Controller = LeastClassTaughtController()
result = Controller.GET_LEAST_CLASS()


# Create DataFrame
data = pd.DataFrame(
    {
        "Total": [int(r["total"]) for r
                  in result],
    },
    index=[f"CID: {r['cid']}, {r['cname']} {r['ccode']}" for r in result]
)


fig = px.bar(data, y="Total")
st.plotly_chart(fig)