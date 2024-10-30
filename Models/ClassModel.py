from config import *



class ClassDAO:
    def __init__(self):
        self.connection = psycopg2.connect(**db_params)#Connecting to the database;
        self.cursor = self.connection.cursor()
    
    def getAllData(self):
        query = "SELECT cid,cname,ccode,cdesc,term,years,cred,csyllabus FROM CLASS;"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
    

    def GetClassByCID(self,cid):#CID
        query = "SELECT cid,cname,ccode,cdesc,term,years,cred,csyllabus FROM CLASS WHERE cid = %s;"
        self.cursor.execute(query,(cid,))
        result = self.cursor.fetchone()
        return result


    def InsertClass(self,data):

        try:
            query = "INSERT INTO CLASS(cname,ccode,cdesc,term,years,cred,csyllabus) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            self.cursor.execute(query,(data["cname"],data["ccode"],data["cdesc"],data["term"],data["years"],data["cred"],data["csyllabus"],))
            self.connection.commit()
            return {"message": "Class inserted successfully"}, 201
        except Exception as e:
            print(f"Insertion error: {e}")
            return {"error": str(e)}, 401 


    def UpdateClass(self,data):
        try:
            query = "UPDATE CLASS SET cname = %s ,ccode = %s ,cdesc = %s ,term = %s ,years = %s ,cred = %s ,csyllabus = %s"
            self.cursor.execute(query,(data["cname"],data["ccode"],data["cdesc"],data["term"],data["years"],data["cred"],data["csyllabus"],))
            self.connection.commit()
            return {"message": "Class updated successfully"},400
        except Exception as e:
            print(f"Update error: {e}")
            return {"error": str(e)}, 200


    def DeleteClassByCID(self,cid):
        try:
            query = "DELETE FROM CLASS WHERE cid = %s;"
            self.cursor.execute(query,(cid,))
            self.connection.commit()
            return {"message":"CLass has been deleted"},200
        except Exception as e:
            print(f"Delete error: {e}")
            return {"error": str(e)}, 400
    
    
    
        
    def Make_Dictionary(self,data): #data is a list of tuples
        result = {}
        result["cid"] = data[0]
        result["cname"] = data[1]
        result["ccode"] = data[2]
        result["cdesc"] = data[3]
        result["term"] = data[4]
        result["years"] = data[5]
        result["cred"] = data[6]
        result["csyllabus"] = data[7]
        return result

    


