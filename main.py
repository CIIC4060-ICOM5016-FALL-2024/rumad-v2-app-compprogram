#--------------------#IMPORTS#--------------------#

from flask import Flask,render_template,jsonify

from flask_cors import CORS
from config import *
#--------------------#APP_INITIALIZED#--------------------#
cursor = connection.cursor()
app = Flask(__name__)
CORS(app)



@app.route("/")
def home():
    query = "SELECT * FROM CLASS;"
    cursor.execute(query)
    result = cursor.fetchall()
    return jsonify(result)







#--------------------#RUN_SERVER#--------------------#

if __name__ == "__main__":
    app.run(debug=True)