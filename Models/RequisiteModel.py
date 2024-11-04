from config import *



class RequisiteDAO:
    def __init__(self):
        self.connection = psycopg2.connect(**db_params)#Connecting to the database;
        self.cursor = self.connection.cursor()
    
    def getAllRequisites(self):
        query = "SELECT classid, reqid, prereq FROM Requisite;"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result


    def GetRequisiteByPrimaryKey(self,classid,reqid):#MID
        query = "SELECT classid, reqid, prereq FROM Requisite WHERE classid = %s AND reqid = %s;"
        self.cursor.execute(query,(classid,reqid,))
        result = self.cursor.fetchone()
        if result is None:
            print(f"No record found for PrimaryKey: ({classid},{reqid})")  # Debug: Log missing record
            return {"error": f"No Requisite found with PrimaryKey ({classid},{reqid})"}, 404
        return result



    def InsertRequisite(self,data):
        query = "INSERT INTO Requisite(classid, reqid, prereq) VALUES(%s,%s,%s)"
        self.cursor.execute(query,(data["classid"],data["reqid"],data["prereq"],))
        self.connection.commit()
        return {"message": "Requisite inserted successfully"}, 201



    def UpdateRequisite(self,data):
        query = "UPDATE Requisite SET prereq = %s WHERE classid = %s and reqid = %s;"
        self.cursor.execute(query,(data["prereq"],data["classid"],data["reqid"],))
        self.connection.commit()
        if self.cursor.rowcount > 0:
            return {"message": "Requisite updated successfully"}, 200
        else:
            return {"message": "Requisite not found"}, 404  # No Requisite was found to delete


    def DeleteRequisiteByPrimaryKey(self,classid,reqid):
        query = "DELETE FROM Requisite WHERE classid = %s AND reqid = %s;"
        self.cursor.execute(query,(classid,reqid,))
        self.connection.commit()
        if self.cursor.rowcount > 0:
            return {"message": "Requisite has been deleted"}, 200
        else:
            return {"message": "Requisite not found"}, 404  # No Requisite was found to delete
    
    
    
    def Make_Dictionary(self,data): #data is a list of tuples
        result = {}
        result["classid"] = data[0]
        result["reqid"] = data[1]
        result["prereq"] = str(data[2])
        return result
    


