from config import *



class MeetingDAO:
    def __init__(self):
        self.connection = psycopg2.connect(**db_params)#Connecting to the database;
        self.cursor = self.connection.cursor()
    
    def getAllMeetings(self):
        query = "SELECT mid, ccode, starttime, endtime, cdays FROM Meeting;"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
    

    def GetMeetingByMID(self,mid):#MID
        query = "SELECT mid, ccode, starttime, endtime, cdays FROM Meeting WHERE mid = %s;"
        self.cursor.execute(query,(mid,))
        result = self.cursor.fetchone()
        if result is None:
            print(f"No record found for MID: {mid}")  # Debug: Log missing record
            return {"error": f"No Meeting found with MID {mid}"}, 404
        return result



    def InsertMeeting(self,data):
        query = "INSERT INTO Meeting(ccode, starttime, endtime, cdays) VALUES(%s,%s,%s,%s)"
        self.cursor.execute(query,(data["ccode"],data["starttime"],data["endtime"],data["cdays"],))
        self.connection.commit()
        return {"message": "Meeting inserted successfully"}, 201



    def UpdateMeeting(self,data):
        query = "UPDATE Meeting SET ccode = %s ,starttime = %s ,endtime = %s ,cdays = %s WHERE mid = %s"
        self.cursor.execute(query,(data["ccode"],data["starttime"],data["endtime"],data["cdays"],data["mid"],))
        self.connection.commit()
        if self.cursor.rowcount > 0:
            return {"message": "Meeting updated successfully"}, 200
        else:
            return {"message": "Meeting not found"}, 404  # No Meeting was found to delete


    def DeleteMeetingByMID(self,mid):
        query = "DELETE FROM Meeting WHERE mid = %s;"
        self.cursor.execute(query,(mid,))
        self.connection.commit()
        if self.cursor.rowcount > 0:
            return {"message": "Meeting has been deleted"}, 200
        else:
            return {"message": "Meeting not found"}, 404  # No Meeting was found to delete
    
    
    
    def Make_Dictionary(self,data): #data is a list of tuples
        result = {}
        result["mid"] = data[0]
        result["ccode"] = data[1]
        result["starttime"] = str(data[2])
        result["endtime"] = str(data[3])
        result["cdays"] = data[4]
        return result
    


