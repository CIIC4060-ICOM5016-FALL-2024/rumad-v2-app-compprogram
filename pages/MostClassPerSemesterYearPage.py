from Controllers.MostClassPerSemesterYearController import MostClassPerSemesterYearController
import streamlit as st
import plotly.express as px
import pandas as pd
st.title("Top 3 most taught classes per semester per year")


try:
    semester = st.selectbox("Choose a Semester",["V1","V2","Spring","Fall"])
    betweenYears = list(range(2017,2026))
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
