#--------------------#IMPORTS#--------------------#

from flask import Flask,render_template,jsonify
from Models.ClassModel import ClassDAO
from Controllers.ClassController import ClassController

from flask_cors import CORS
from config import *
#--------------------#APP_INITIALIZED#--------------------#
app = Flask(__name__)
CORS(app)


#----------------TABLE CLASS------------------------------------------------------------------------------------


#----------GET ALL DATA FOR CLASS
@app.route("/compprogram/class",methods=["GET"])
def GetAllData():
    classObj = ClassDAO()
    list = []
    data = classObj.getAllData()
    for row in data:
        list.append(classObj.Make_Dictionary(row))
    return jsonify(list)

#-------GET ALL DATA FOR A CLASS BY CID

@app.route("/compprogram/class/<int:cid>",methods=["GET"])
def GetClassByCID(cid):
    classObj = ClassDAO()
    data = classObj.GetClassByCID(cid)
    result = classObj.Make_Dictionary(data)
    return jsonify(result)

#----------------TABLE CLASS------------------------------------------------------------------------------------






#--------------------#RUN_SERVER#--------------------#

if __name__ == "__main__":
    app.run(debug=True)