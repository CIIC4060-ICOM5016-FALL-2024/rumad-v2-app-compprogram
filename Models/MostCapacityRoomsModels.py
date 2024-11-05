from config import *

class MostCapacityRoomsDAO:
    def __init__(self):
        self.connection = psycopg2.connect(**db_params)
        self.cursor = self.connection.cursor()
        
    def GET_Most_Capacity_Rooms(self,building):
        query = """SELECT rid, building, room_number, capacity 
        FROM ROOM
        WHERE building = %s 
        ORDER BY capacity DESC 
        LIMIT 3;"""
        self.cursor.execute(query,(building,))
        result = self.cursor.fetchall()
        return result
    
    
    def Make_Dictionary(self,data):
        result = {}
        result["rid"] = data[0]
        result["building"] = data[1]
        result["room_number"] = data[2]
        result["capacity"] = data[3]
        return result