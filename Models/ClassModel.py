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

    


