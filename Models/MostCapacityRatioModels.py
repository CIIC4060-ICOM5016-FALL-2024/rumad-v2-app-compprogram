from config import *

class MostCapacityRatioDAO:
    def __init__(self):
        self.connection = psycopg2.connect(**db_params)
        self.cursor = self.connection.cursor()
        
    def GET_MOST_CAPACITY_RATIO(self,rid):
        query = """SELECT rid,room_number, section.sid,(section.capacity::Float)/(room.capacity::Float) * 100  as student_to_capacity_ratio
                    FROM section
                    INNER JOIN room
                    ON room.rid = section.roomid
                    WHERE rid = %s
                    ORDER BY student_to_capacity_ratio DESC
                    LIMIT 3;"""
        self.cursor.execute(query,(rid,))
        result = self.cursor.fetchall()
        if len(result) == 0:
            return Exception
        return result
    
    
    def Make_Dictionary(self,data):
        result = {}
        result["rid"] = data[0]
        result["room_number"] = data[1]
        result["sid"] = data[2]
        result["student_to_capacity_ratio"] = data[3]
        return result