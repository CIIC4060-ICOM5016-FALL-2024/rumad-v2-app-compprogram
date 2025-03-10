from config import *



class SyllabusDAO:
    def __init__(self):
        self.connection = psycopg2.connect(**db_params)#Connecting to the database;
        self.cursor = self.connection.cursor()
    
    def GetAllSyllabus(self):
        query = "SELECT chunkid, courseid, embedding_text, chunk FROM Syllabus;"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result



    def GetSyllabusByCHUNKID(self,chunkid):#CHUNKID
        query = "SELECT chunkid,courseid, embedding_text, chunk FROM Syllabus WHERE chunkid = %s;"
        self.cursor.execute(query,(chunkid,))
        result = self.cursor.fetchone()
        if result is None:
            print(f"No record found for CHUNKID: {chunkid}")  # Debug: Log missing record
            return {"error": f"No Syllabus found with CHUNKID {chunkid}"}, 404
        print(result)
        return result



    def InsertSyllabus(self,data):
        query = "INSERT INTO Syllabus(courseid, embedding_text, chunk) VALUES(%s,%s,%s)"
        self.cursor.execute(query,(data["courseid"],data["embedding_text"],data["chunk"],))
        self.connection.commit()
        return {"message": "Syllabus inserted successfully"}, 201



    def UpdateSyllabus(self,data):
        query = "UPDATE Syllabus SET courseid = %s ,embedding_text = %s ,chunk = %s WHERE chunkid = %s"
        self.cursor.execute(query,(data["courseid"],data["embedding_text"],data["chunk"],data["chunkid"],))
        self.connection.commit()
        if self.cursor.rowcount > 0:
            return {"message": "Syllabus updated successfully"}, 200
        else:
            return {"message": "Syllabus not found"}, 404  # No Syllabus was found to delete


    def DeleteSyllabusByCHUNKID(self,chunkid):
        query = "DELETE FROM Syllabus WHERE chunkid = %s;"
        self.cursor.execute(query,(chunkid,))
        self.connection.commit()
        if self.cursor.rowcount > 0:
            return {"message": "Syllabus has been deleted"}, 200
        else:
            return {"message": "Syllabus not found"}, 404  # No Syllabus was found to delete
    
    
    
        
    def Make_Dictionary(self,data): #data is a list of tuples
        result = {}
        result["chunkid"] = data[0]
        result["courseid"] = data[1]
        result["embedding_text"] = data[2]
        result["chunk"] = data[3]
        return result

    


