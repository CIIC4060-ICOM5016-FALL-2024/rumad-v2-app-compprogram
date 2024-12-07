from Controllers.SectionsPerYearController import SectionsPerYearController
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
        
    st.title("Total number of sections per year")


    Controller = SectionsPerYearController()
    result = Controller.GET_SECTIONS_PER_YEAR()


    # Create DataFrame
    data = pd.DataFrame(
        {
            "sections_per_year": [int(r["sections_per_year"]) for r
                    in result],
        },
        index=[f"Years: {r['years']}" for r in result]
    )


    fig = px.bar(data, y="sections_per_year")
    st.plotly_chart(fig)