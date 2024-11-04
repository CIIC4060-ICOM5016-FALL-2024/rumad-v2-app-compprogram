from config import *



class RoomDAO:
    def __init__(self):
        self.connection = psycopg2.connect(**db_params)#Connecting to the database;
        self.cursor = self.connection.cursor()
    
    def GetAllRooms(self):
        query = "SELECT rid, building, room_number, capacity FROM Room;"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
    

    def GetRoomByRID(self,rid):#RID
        query = "SELECT rid, building, room_number, capacity FROM Room WHERE rid = %s;"
        self.cursor.execute(query,(rid,))
        result = self.cursor.fetchone()
        if result is None:
            print(f"No record found for RID: {rid}")  # Debug: Log missing record
            return {"error": f"No Room found with RID {rid}"}, 404
        return result



    def InsertRoom(self,data):
        query = "INSERT INTO Room(building,room_number, capacity) VALUES(%s,%s,%s)"
        self.cursor.execute(query,(data["building"],data["room_number"],data["capacity"],))
        self.connection.commit()
        return {"message": "Room inserted successfully"}, 201



    def UpdateRoom(self,data):
        query = "UPDATE Room SET building = %s ,room_number = %s ,capacity = %s WHERE rid = %s"
        self.cursor.execute(query,(data["building"],data["room_number"],data["capacity"],data["rid"],))
        self.connection.commit()
        if self.cursor.rowcount > 0:
            return {"message": "Room updated successfully"}, 200
        else:
            return {"message": "Room not found"}, 404  # No Room was found to delete


    def DeleteRoomByRID(self,rid):
        query = "DELETE FROM Room WHERE rid = %s;"
        self.cursor.execute(query,(rid,))
        self.connection.commit()
        if self.cursor.rowcount > 0:
            return {"message": "Room has been deleted"}, 200
        else:
            return {"message": "Room not found"}, 404  # No Room was found to delete
    
    
    
        
    def Make_Dictionary(self,data): #data is a list of tuples
        result = {}
        result["rid"] = data[0]
        result["building"] = data[1]
        result["room_number"] = data[2]
        result["capacity"] = data[3]
        return result

    


