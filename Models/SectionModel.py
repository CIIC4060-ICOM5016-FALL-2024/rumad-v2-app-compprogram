from config import *



class SectionDAO:
    def __init__(self):
        self.connection = psycopg2.connect(**db_params)#Connecting to the database;
        self.cursor = self.connection.cursor()
    
    def getAllSections(self):
        query = "SELECT sid, roomid, cid, mid, semester, years, capacity FROM SECTION;"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
    

    def GetSectionBySID(self,sid):#SID
        query = "SELECT sid, roomid, cid, mid, semester, years, capacity FROM SECTION WHERE sid = %s;"
        self.cursor.execute(query,(sid,))
        result = self.cursor.fetchone()
        if result is None:
            print(f"No record found for CID: {sid}")  # Debug: Log missing record
            return {"error": f"No section found with SID {sid}"}, 404
        return result



    def InsertSection(self,data):
        query = "INSERT INTO SECTION(roomid, cid, mid, semester, years, capacity ) VALUES(%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(query,(data["roomid"],data["cid"],data["mid"],data["semester"],data["years"],data["capacity"],))
        self.connection.commit()
        return {"message": "Section inserted successfully"}, 201



    def UpdateSection(self,data):
        query = "UPDATE SECTION SET roomid = %s ,cid = %s ,mid = %s ,semester = %s ,years = %s ,capacity = %s WHERE sid = %s"
        self.cursor.execute(query,(data["roomid"],data["cid"],data["mid"],data["semester"],data["years"],data["capacity"],data["sid"],))
        self.connection.commit()
        if self.cursor.rowcount > 0:
            return {"message": "Section updated successfully"}, 200
        else:
            return {"message": "Section not found"}, 404  # No section was found to delete


    def DeleteSectionBySID(self,sid):
        query = "DELETE FROM SECTION WHERE sid = %s;"
        self.cursor.execute(query,(sid,))
        self.connection.commit()
        if self.cursor.rowcount > 0:
            return {"message": "Section has been deleted"}, 200
        else:
            return {"message": "Section not found"}, 404  # No section was found to delete
    
    
    
    def Make_Dictionary(self,data): #data is a list of tuples
        result = {}
        result["sid"] = data[0]
        result["roomid"] = data[1]
        result["cid"] = data[2]
        result["mid"] = data[3]
        result["semester"] = data[4]
        result["years"] = data[5]
        result["capacity"] = data[6]
        return result

    


