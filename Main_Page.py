from main import *
import pandas as pd


page = st.selectbox("Choose a page", ["Home", "All Classes", "All Rooms","All Sections","All Meetings","All Requisites"])
st.session_state.page = page

if st.session_state.page == "Home":
    # Render home page content
    st.header("Welcome to the New Putty")
    st.write("In the side bar, you can see all the different options for all the local and Global Statistics")
    st.write("Also, in the current Drop Down list you can verify all the information of all the tables")
elif st.session_state.page == "All Classes":
    Controller = ClassController()
    result = Controller.GetAllClasses()
    order_result = pd.DataFrame(result)
    st.dataframe(order_result,use_container_width=True)
elif st.session_state.page == "All Rooms":
    Controller = RoomController()
    result = Controller.GetAllRooms()
    order_result = pd.DataFrame(result)
    st.dataframe(order_result,use_container_width=True)
elif st.session_state.page == "All Sections":
    Controller = SectionController()
    result = Controller.GetAllSections()
    order_result = pd.DataFrame(result)
    st.dataframe(order_result,use_container_width=True)
elif st.session_state.page == "All Meetings":
    Controller = MeetingController()
    result = Controller.GetAllMeetings()
    order_result = pd.DataFrame(result)
    st.dataframe(order_result,use_container_width=True)
elif st.session_state.page == "All Requisites":
    Controller = RequisiteController()
    result = Controller.GetAllRequisites()
    order_result = pd.DataFrame(result)
    st.dataframe(order_result,use_container_width=True)
    