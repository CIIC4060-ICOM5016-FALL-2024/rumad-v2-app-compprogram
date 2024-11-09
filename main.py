#--------------------#IMPORTS#--------------------#

from flask import Flask,render_template,jsonify,request
#------------CONTROLLERS----------------------------------------------------

from Controllers.ClassController import ClassController
from Controllers.SectionController import SectionController
from Controllers.MeetingController import MeetingController
from Controllers.RequisiteController import RequisiteController
from Controllers.RoomController import RoomController
from Controllers.SyllabusController import SyllabusController
from Controllers.MostCapacityRoomsController import MostCapacityRoomsController
from Controllers.MostCapacityRatioController import MostCapacityRatioController
from Controllers.MeetingMostSectionController import MeetingMostSectionController
from Controllers.MostClassPerRoomController import MostClassPerRoomController
from Controllers.MostPrerequisiteController import MostPrerequisiteController
from Controllers.MostClassPerSemesterYearController import MostClassPerSemesterYearController
from Controllers.LeastClassTaughtController import LeastClassTaughtController
from Controllers.SectionsPerYearController import SectionsPerYearController
#----------------------------------------------------------------

from flask_cors import CORS
from config import *
#--------------------#APP_INITIALIZED#--------------------#
app = Flask(__name__)
CORS(app)

#----------------WELCOME-------------------------------------------------------------------------------------------------
@app.route("/")
def home():
    return "Welcome to the New Putty"
#----------------TABLE CLASS------------------------------------------------------------------------------------

@app.route("/compprogram/class",methods=["GET","POST"])

def HandlerCLass():
    if request.method == "GET":
        return GetAllClasses()
    elif request.method == "POST":
        return InsertClass()

#----------GET ALL DATA FOR CLASS------------------
def GetAllClasses():
    Controller = ClassController()
    return jsonify(Controller.GetAllClasses())
#-------INSERT NEW CLASS---------------------------
def InsertClass():
    Controller = ClassController()
    data = request.get_json()
    return Controller.InsertClass(data)


#-------GET ALL DATA FOR A CLASS BY CID------------

@app.route("/compprogram/class/<cid>",methods=["GET"])
        
def GetClassByCID(cid):
    Controller = ClassController()
    return jsonify(Controller.GetClassByCID(cid))


#-------UPDATE AN EXISTENT CLASS---------------------------
@app.route("/compprogram/class/<cid>",methods=["PUT"])

def UpdateClass(cid):
    Controller = ClassController()
    data = request.get_json()
    return Controller.UpdateClass(cid,data)

#-------DELETE CLASS BY CID------------------------


@app.route("/compprogram/class/<cid>",methods=["DELETE"])

def DeleteCLassByCID(cid):
    Controller = ClassController()
    return Controller.DeleteClassByCID(cid)

#----------------TABLE CLASS------------------------------------------------------------------------------------




#----------------TABLE SECTION------------------------------------------------------------------------------------

@app.route("/compprogram/section",methods=["GET","POST","PUT"])

def HandlerSection():
    if request.method == "GET":
        return GetAllSections()
    elif request.method == "POST":
        return InsertSection()
    elif request.method == "PUT":
        return UpdateSection()
#----------GET ALL DATA FOR SECTIONS------------------
def GetAllSections():
    Controller = SectionController()
    return jsonify(Controller.GetAllSections())
#-------INSERT NEW SECTIONS---------------------------
def InsertSection():
    Controller = SectionController()
    data = request.get_json()
    return Controller.InsertSection(data)

#-------UPDATE AN EXISTENT SECTION---------------------------

def UpdateSection():
    Controller = SectionController()
    data = request.get_json()
    return Controller.UpdateSection(data)


#-------GET ALL DATA FOR A SECTION BY SID------------

@app.route("/compprogram/section/<sid>",methods=["GET"])
        
def GetSectionBySID(sid):
    Controller = SectionController()
    return jsonify(Controller.GetSectionBySID(sid))

#-------DELETE SECTION BY SID------------------------


@app.route("/compprogram/section/<sid>",methods=["DELETE"])

def DeleteSectionBySID(sid):
    Controller = SectionController()
    return Controller.DeleteSectionBySID(sid)

#----------------TABLE SECTION------------------------------------------------------------------------------------



#----------------TABLE MEETING------------------------------------------------------------------------------------



@app.route("/compprogram/meeting",methods=["GET","POST","PUT"])

def HandlerMeeting():
    if request.method == "GET":
        return GetAllMeetings()
    elif request.method == "POST":
        return InsertMeeting()
    elif request.method == "PUT":
        return UpdateMeeting()
#----------GET ALL DATA FOR MEETINGS------------------
def GetAllMeetings():
    Controller = MeetingController()
    return jsonify(Controller.GetAllMeetings())
#-------INSERT NEW MEETINGS---------------------------
def InsertMeeting():
    Controller = MeetingController()
    data = request.get_json()
    return Controller.InsertMeeting(data)

#-------UPDATE AN EXISTENT MEETING---------------------------

def UpdateMeeting():
    Controller = MeetingController()
    data = request.get_json()
    return Controller.UpdateMeeting(data)


#-------GET ALL DATA FOR A MEETING BY MID------------

@app.route("/compprogram/meeting/<mid>",methods=["GET"])
        
def GetMeetingByMID(mid):
    Controller = MeetingController()
    return jsonify(Controller.GetMeetingByMID(mid))

#-------DELETE MEETING BY MID------------------------


@app.route("/compprogram/meeting/<mid>",methods=["DELETE"])

def DeleteMeetingByMID(mid):
    Controller = MeetingController()
    return Controller.DeleteMeetingByMID(mid)



#----------------TABLE MEETING------------------------------------------------------------------------------------


#----------------TABLE REQUISITE------------------------------------------------------------------------------------

@app.route("/compprogram/requisite",methods=["GET","POST","PUT"])

def HandlerRequisite():
    if request.method == "GET":
        return GetAllRequisites()
    elif request.method == "POST":
        return InsertRequisite()
    elif request.method == "PUT":
        return UpdateRequisite()
#----------GET ALL DATA FOR REQUISITE------------------
def GetAllRequisites():
    Controller = RequisiteController()
    return jsonify(Controller.GetAllRequisites())
#-------INSERT NEW REQUISITE---------------------------
def InsertRequisite():
    Controller = RequisiteController()
    data = request.get_json()
    return Controller.InsertRequisite(data)

#-------UPDATE AN EXISTENT REQUISITE---------------------------

def UpdateRequisite():
    Controller = RequisiteController()
    data = request.get_json()
    return Controller.UpdateRequisite(data)


#-------GET ALL DATA FOR A REQUISITE BY PrimaryKey------------

@app.route("/compprogram/requisite/<classid>/<reqid>",methods=["GET"])
        
def GetRequisiteByPrimaryKey(classid,reqid):
    Controller = RequisiteController()
    return jsonify(Controller.GetRequisiteByPrimaryKey(classid,reqid))

#-------DELETE REQUISITE BY PrimaryKey------------------------


@app.route("/compprogram/requisite/<classid>/<reqid>",methods=["DELETE"])

def DeleteRequisiteByPrimaryKey(classid,reqid):
    Controller = RequisiteController()
    return Controller.DeleteRequisiteByPrimaryKey(classid,reqid)


#----------------TABLE REQUISITE------------------------------------------------------------------------------------

#----------------TABLE ROOM------------------------------------------------------------------------------------



@app.route("/compprogram/room",methods=["GET","POST","PUT"])

def HandlerRoom():
    if request.method == "GET":
        return GetAllRooms()
    elif request.method == "POST":
        return InsertRoom()
    elif request.method == "PUT":
        return UpdateRoom()
#----------GET ALL DATA FOR ROOMS------------------
def GetAllRooms():
    Controller = RoomController()
    return jsonify(Controller.GetAllRooms())
#-------INSERT NEW ROOMS---------------------------
def InsertRoom():
    Controller = RoomController()
    data = request.get_json()
    return Controller.InsertRoom(data)

#-------UPDATE AN EXISTENT ROOM---------------------------

def UpdateRoom():
    Controller = RoomController()
    data = request.get_json()
    return Controller.UpdateRoom(data)


#-------GET ALL DATA FOR A ROOM BY RID------------

@app.route("/compprogram/room/<rid>",methods=["GET"])
        
def GetRoomByRID(rid):
    Controller = RoomController()
    return jsonify(Controller.GetRoomByRID(rid))

#-------DELETE ROOM BY RID------------------------


@app.route("/compprogram/room/<rid>",methods=["DELETE"])

def DeleteRoomByRID(rid):
    Controller = RoomController()
    return Controller.DeleteRoomByRID(rid)


#----------------TABLE ROOM------------------------------------------------------------------------------------


#----------------TABLE SYLLABUS------------------------------------------------------------------------------------



@app.route("/compprogram/syllabus",methods=["GET","POST","PUT"])

def HandlerSyllabus():
    if request.method == "GET":
        return GetAllSyllabus()
    elif request.method == "POST":
        return InsertSyllabus()
    elif request.method == "PUT":
        return UpdateSyllabus()
#----------GET ALL DATA FOR SYLLABUS------------------
def GetAllSyllabus():
    Controller = SyllabusController()
    return jsonify(Controller.GetAllSyllabus())
#-------INSERT NEW SYLLABUS---------------------------
def InsertSyllabus():
    Controller = SyllabusController()
    data = request.get_json()
    return Controller.InsertSyllabus(data)

#-------UPDATE AN EXISTENT SYLLABUS---------------------------

def UpdateSyllabus  ():
    Controller = SyllabusController()
    data = request.get_json()
    return Controller.UpdateSyllabus(data)


#-------GET ALL DATA FOR A SYLLABUS BY CHUNKID------------

@app.route("/compprogram/syllabus/<chunkid>",methods=["GET"])
        
def GetSyllabusByCHUNKID(chunkid):
    Controller = SyllabusController()
    return jsonify(Controller.GetSyllabusByCHUNKID(chunkid))

#-------DELETE ROOM BY CHUNKID------------------------


@app.route("/compprogram/syllabus/<chunkid>",methods=["DELETE"])

def DeleteSyllabusByCHUNKID(chunkid):
    Controller = SyllabusController()
    return Controller.DeleteSyllabusByCHUNKID(chunkid)


#----------------TABLE SYLLABUS------------------------------------------------------------------------------------

#/*------------------------------Local Statistics------------------------------------------------------*/
#--------------------------------Top 3 rooms with the most capacity-------------------------------

@app.route("/compprogram/room/<building>/capacity",methods=["GET"])
def GET_MOST_CAPACITY_ROOMS(building):
    Controller = MostCapacityRoomsController()
    return jsonify(Controller.GET_Most_Capacity_Rooms(building))


#----------------------------------------------------------------------------------------------------------
#----------------------------------------Top 3 sections with the most student-to-capacity ratio.----------------

@app.route("/compprogram/room/<rid>/ratio",methods=["GET"])
def GET_MOST_CAPACITY_RATIO(rid):
    Controller = MostCapacityRatioController()
    return jsonify(Controller.GET_MOST_CAPACITY_RATIO(rid))


#----------------------------------------Top 3 classes that where taught the most per room-----------------------------------------------------------------------
@app.route("/compprogram/room/<rid>/classes",methods=["GET"])
def GET_Most_Class_Per_Room(rid):
    Controller = MostClassPerRoomController()
    return jsonify(Controller.GET_Most_Class_Per_Room(rid))


#--/*------------------------------------Top 3 most taught classes per semester per year-------------------------------------------------*/

@app.route("/compprogram/classes/<years>/<semester>", methods= ["GET"])
def GET_Most_CLass_Per_Semester_Year(years,semester):
    controller = MostClassPerSemesterYearController()
    return jsonify(controller.GET_Most_CLass_Per_Semester_Year(years,semester))

#/*------------------------------Global Statistics------------------------------------------------------*/



#----------------------------------Top 5 meetings with the most sections------------------------------

@app.route("/compprogram/most/meeting", methods = ["GET"])
def GET_MEETING_WITH_MOST_SECTION():
    controller = MeetingMostSectionController()
    return jsonify(controller.GET_MEETING_WITH_MOST_SECTION())

#----------------------------------Top 3 classes that appears the most as prerequisite to other classes----------------------------------------------------------------------

@app.route("/compprogram/most/prerequisite", methods = ["GET"])
def GET_TOP_PREQUISITE():
    controller = MostPrerequisiteController()
    return jsonify(controller.GET_TOP_PREREQUISITE())


#--/*-------------------------------------------------------------------------------------*/


#--/*------------------------------Top 3 classes that were offered the least----------------------------------------------------------*/

@app.route("/compprogram/least/classes", methods = ["GET"])
def GET_LEAST_CLASS():
    controller = LeastClassTaughtController()
    return jsonify(controller.GET_LEAST_CLASS())

#--/*------------------------------Total number of sections per year----------------------------------------------------------*/

@app.route("/compprogram/section/year", methods = ["GET"])
def GET_SECTIONS_PER_YEAR():
    controller = SectionsPerYearController()
    return jsonify(controller.GET_SECTIONS_PER_YEAR())

if __name__ == "__main__":
    app.run(debug=True)