#--------------------#IMPORTS#--------------------#

from flask import Flask,render_template,jsonify,request
#------------MODELS----------------------------------------------------
from Models.ClassModel import ClassDAO
from Models.SectionModel import SectionDAO
from Models.MeetingModel import MeetingDAO
from Models.RequisiteModel import RequisiteDAO
#----------------------------------------------------------------
#------------CONTROLLERS----------------------------------------------------

from Controllers.ClassController import ClassController
from Controllers.SectionController import SectionController
from Controllers.MeetingController import MeetingController
from Controllers.RequisiteController import RequisiteController
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

@app.route("/compprogram/class",methods=["GET","POST","PUT"])

def HandlerCLass():
    if request.method == "GET":
        return GetAllClasses()
    elif request.method == "POST":
        return InsertClass()
    elif request.method == "PUT":
        return UpdateClass()
#----------GET ALL DATA FOR CLASS------------------
def GetAllClasses():
    Controller = ClassController()
    return jsonify(Controller.GetAllClasses())
#-------INSERT NEW CLASS---------------------------
def InsertClass():
    Controller = ClassController()
    data = request.get_json()
    return Controller.InsertClass(data)

#-------UPDATE AN EXISTENT CLASS---------------------------

def UpdateClass():
    Controller = ClassController()
    data = request.get_json()
    return Controller.UpdateClass(data)


#-------GET ALL DATA FOR A CLASS BY CID------------

@app.route("/compprogram/class/<cid>",methods=["GET"])
        
def GetClassByCID(cid):
    Controller = ClassController()
    return jsonify(Controller.GetClassByCID(cid))

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

#-------DELETE CLSASS BY CID------------------------


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


#-------GET ALL DATA FOR A SECTION BY MID------------

@app.route("/compprogram/meeting/<mid>",methods=["GET"])
        
def GetMeetingByMID(mid):
    Controller = MeetingController()
    return jsonify(Controller.GetMeetingByMID(mid))

#-------DELETE CLSASS BY CID------------------------


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



#--------------------#RUN_SERVER#--------------------#

if __name__ == "__main__":
    app.run(debug=True)