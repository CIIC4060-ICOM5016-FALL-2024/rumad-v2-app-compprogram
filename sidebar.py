import streamlit as st

def make_sidebar():
    st.sidebar.page_link("Main_Page.py", label="Main Page")
    st.sidebar.page_link("pages/chatbot.py", label="Chatbot")
    st.sidebar.page_link("pages/LeastClassTaughtPage.py", label="Least Taught Class")
    st.sidebar.page_link("pages/MeetingMostSectionPage.py", label="Meeting Most Section")
    st.sidebar.page_link("pages/MostCapacityRatioPage.py", label="Most Capacity Ratio")
    st.sidebar.page_link("pages/MostCapacityRoomsPage.py", label="Most Capacity Rooms")
    st.sidebar.page_link("pages/MostClassPerRoomPage.py", label="Most Class Per Room")
    st.sidebar.page_link("pages/MostClassPerSemesterYearPage.py", label="Most Class Per Semester")
    st.sidebar.page_link("pages/MostPrerequisitePage.py", label="Most Prerequisite")
    st.sidebar.page_link("pages/SectionsPerYearPage.py", label="Sections Per Year")