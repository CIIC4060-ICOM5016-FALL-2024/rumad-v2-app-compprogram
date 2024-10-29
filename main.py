#--------------------#IMPORTS#--------------------#

from flask import Flask,render_template,jsonify,request
from Models.ClassModel import ClassDAO
from Controllers.ClassController import ClassController

from flask_cors import CORS
from config import *
#--------------------#APP_INITIALIZED#--------------------#
app = Flask(__name__)
CORS(app)


#----------------TABLE CLASS------------------------------------------------------------------------------------

@app.route("/compprogram/class",methods=["GET","POST","PUT"])

def HandlerCLass():
    if request.method == "GET":
        return GetAllData()
    elif request.method == "POST":
        return InsertClass()
    elif request.method == "PUT":
        return UpdateClass()
#----------GET ALL DATA FOR CLASS------------------
def GetAllData():
    Controller = ClassController()
    return jsonify(Controller.GetAllClass())
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

@app.route("/compprogram/class/<int:cid>",methods=["GET"])
def GetClassByCID(cid):
    Controller = ClassController()
    request.get_data()
    return jsonify(Controller.GetClassByCID(cid))




#----------------TABLE CLASS------------------------------------------------------------------------------------






#--------------------#RUN_SERVER#--------------------#

if __name__ == "__main__":
    app.run(debug=True)