from config import *

# Login
class LoginDao:
    def __init__(self):
        self.connection = psycopg2.connect(**db_params)
        self.cursor = self.connection.cursor()


    def Verification(self,username,password):
        query = """SELECT username,password
        FROM LOGIN
        WHERE username = %s AND password = %s"""
        self.cursor.execute(query,(username,password,))
        result = self.cursor.fetchone()
        return result
    
    def CreateAccount(self,username,password):
        try:
            query = "INSERT INTO Login(username,password) VALUES(%s,%s)"
            self.cursor.execute(query,(username,password,))
            self.connection.commit()
            return 201
        except:
            return 200
        
    
    
    def Make_Dictionary(self,data):
        result = {}
        result["username"] = data[0]
        result["password"] = data[1]
        return result

  
