from config import *

class MostClassPerRoomDAO:
    def __init__(self):
        self.connection = psycopg2.connect(**db_params)
        self.cursor = self.connection.cursor()
        
    def GET_Most_Class_Per_Room(self,cid):
        query = """SELECT concat(class.cname,' ',class.ccode) as ClassName, class.cdesc, room_number, sum(section.capacity) as students
                    FROM class
                    INNER JOIN section
                    ON section.cid = class.cid
                    INNER JOIN room
                    ON section.roomid = room.rid
                    where rid = %s
                    GROUP BY class.cdesc, room_number,class.ccode,class.cname
                    ORDER BY students DESC
                    LIMIT 3;"""
        self.cursor.execute(query,(cid,))
        result = self.cursor.fetchall()
        if len(result) == 0:
            return Exception
        return result
    
    
    def Make_Dictionary(self,data,cid):
        result = {}
        result["cid"] = int(cid)
        result["class Name"] = data[0]
        result["cdesc"] = data[1]
        result["room_number"] = data[2]
        result["students"] = data[3]
        return result