# streamlit_app: Page Title Here

from Controllers.LeastClassTaughtController import LeastClassTaughtController
import streamlit as st
import pandas as pd
import plotly.express as px


if(st.session_state.login_in == False):
    st.write("Please log in to see the data")

    if(st.button("Log in")):
        st.switch_page("Main_page.py")



else:
    st.title("Top 3 classes that were offered the least")


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