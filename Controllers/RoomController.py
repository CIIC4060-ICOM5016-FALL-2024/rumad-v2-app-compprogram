from Models.RoomModel import RoomDAO
from Models.SectionModel import SectionDAO

class RoomController:
    
    def __init__(self):#data should be a jsonfile from the user
        self.Courses = RoomDAO()
        self.SectionDAO = SectionDAO()

    def GetAllRooms(self):
        list = []
        data = self.Courses.GetAllRooms()
        for row in data:
            list.append(self.Courses.Make_Dictionary(row))
        return list
    
    def GetRoomByRID(self,rid):
        try:
            rid = int(rid)
            if rid < 0:
                return {"error": "Room ID must be greater or equal to 0"}, 400
            data = self.Courses.GetRoomByRID(rid)
            return self.Courses.Make_Dictionary(data)
        except:
            try:
                rid = int(rid)
                return {"error": f"No Room found with RID: {rid}"}, 404
            except:
                return {"error":f"This is not valid RID: {rid}"},400
    
    def InsertRoom(self,data):
        try:
            # DO NOT ACCEPT BUILDINGS THAT ARE NOT CALLED, Stefani, Monzon OR Software
            Acceptable_Buildings = ["Stefani","Monzon","Software"]
            if (data["building"] not in Acceptable_Buildings):
                return {"error":f"Is not a valid building: {data['building']}"},400
            if(int(data["capacity"]) < 1):
                return {"error": f"At least 1 person, should be in a room and you have {data['capacity']}"},400
            if(int(data["room_number"]) < 0):
                return {"error":"The rooms must be greater or equal to 0"},400
            return self.Courses.InsertRoom(data)
        except Exception as e:
            try:                                          
                int(data["room_number"])              
                return {"error": f"The capacity must be an integer and your is: {data['capacity']}"}, 400
            except:
                return {"error": f"The room_number must be a number and your is: {data['room_number']}"}, 400                                    
                

    def UpdateRoom(self,data):
        try:
            # DO NOT ACCEPT BUILDINGS THAT ARE NOT CALLED, Stefani, Monzon OR Software
            Acceptable_Buildings = ["Stefani","Monzon","Software"]
            if (data["building"] not in Acceptable_Buildings):
                return {"error":f"Is not a valid building: {data['building']}"},400
            if(int(data["capacity"]) < 1):
                return {"error": f"At least 1 person, should be in a room and you have {data['capacity']}"},400
            if(int(data["room_number"]) < 0):
                return {"error":"The rooms must be greater or equal to 0"},400
            return self.Courses.UpdateRoom(data)
        except Exception as e:
            try:                                          
                int(data["room_number"])              
                int(data["rid"])              
                return {"error": f"The capacity must be an integer and your is: {data['capacity']}"}, 400
            except:
                try:
                    int(data["rid"])
                    return {"error": f"The room_number must be a number and your is: {data['room_number']}"}, 400  
                except: 
                    return {"error":f"The rid must be an interger and your is: {data['rid']}"}, 400

    def DeleteRoomByRID(self,rid):
        try:
            rid = int(rid)
            if(rid < 0):
                return {"error":f"The rid must be greater than 0 and your is: {rid}"},400
            return self.Courses.DeleteRoomByRID(rid)
        except Exception as e:
            try:
                int(rid)
                return {"error": str(e)}, 400
            except:
                return {"error": f"The rid must be an integer and your is: {rid}"}, 400
            
                
        