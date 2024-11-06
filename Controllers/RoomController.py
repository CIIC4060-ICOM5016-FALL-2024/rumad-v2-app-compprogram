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
            return {"error": f"This is not a valid rid: {rid}"}
    
    def InsertRoom(self,data):
        try:
            if (data["building"] != "Stefani" and data["building"] != "Monzon" and data["building"] != "Software"):
                return {"error":f"Is not a valid building: {data["building"]}"}
            if(int(data["capacity"]) < 1):
                return {"error": f"At least 1 person, should be in a room and you have {data["capacity"]}"}
            if(int(data["room_number"]) < 0):
                return {"error":"The rooms must be greater or equal to 0"}
            return self.Courses.InsertRoom(data)
        except Exception as e:
            print(f"Insertion error: {e}")
            return {"error": str(e)}, 400

    def UpdateRoom(self,data):
        try:
            if (data["building"] != "Stefani" and data["building"] != "Monzon" and data["building"] != "Software"):
                return {"error":f"Is not a valid building: {data["building"]}"}
            if(int(data["capacity"]) < 1):
                return {"error": f"At least 1 person, should be in a room and you have {data["capacity"]}"}
            if(int(data["room_number"]) < 0):
                return {"error":"The rooms must be greater or equal to 0"}
            return self.Courses.UpdateRoom(data)
        except Exception as e:
            print(f"Update error: {e}")
            return {"error": str(e)}, 400

    def DeleteRoomByRID(self,rid):
        try:
            # self.SectionDAO.DeleteSectionBySID()
            rid = int(rid)
            return self.Courses.DeleteRoomByRID(rid)
        except Exception as e:
            print(f"Delete error: {e}")
            return {"error": str(e)}, 400
        