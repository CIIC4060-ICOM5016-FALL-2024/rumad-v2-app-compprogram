from Controllers.MostClassPerSemesterYearController import MostClassPerSemesterYearController
import streamlit as st
import plotly.express as px
import pandas as pd
from sidebar import make_sidebar
make_sidebar()

if "login_in" not in st.session_state:
    st.session_state.login_in = False

if(st.session_state.login_in == False):
    st.write("Please log in to see the data")

    if(st.button("Log in")):
        st.switch_page("Main_page.py")

else:
        
    st.title("Top 3 most taught classes per semester per year")


    try:
        semester = st.selectbox("Choose a Semester",["V1","V2","Spring","Fall"])
        years = MostClassPerSemesterYearController()
        betweenYears = years.Get_Years()
        year = str(st.selectbox("Pick a year", betweenYears))
        int(year)#Just coroborate that is a number

        Controller = MostClassPerSemesterYearController()
        result = Controller.GET_Most_CLass_Per_Semester_Year(year,semester)
        isClicked = st.button("Send data")
        if isClicked:
            # Create DataFrame
            data = pd.DataFrame(
                {
                    "Class Count": [r["Class Count"] for r in result],
                    "Class Info": [f"Class: {r['Class Name']}" for r in result]  # Creating a new column called room_info
                    #contains the rid and the room_number
                }
            )

            fig = px.bar(data, x="Class Info", y="Class Count")
            st.plotly_chart(fig)
    except:
        st.write("There is no register of a class in that Year and Semester")
