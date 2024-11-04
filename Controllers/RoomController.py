from Models.RoomModel import RoomDAO

class RoomController:
    
    def __init__(self):#data should be a jsonfile from the user
        self.Courses = RoomDAO()

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
        except Exception as e:
            return {"error": f"This is not a valid rid: {rid}"}
    
    def InsertRoom(self,data):
        try:
            return self.Courses.InsertRoom(data)
        except Exception as e:
            print(f"Insertion error: {e}")
            return {"error": str(e)}, 400

    def UpdateRoom(self,data):
        try:
            return self.Courses.UpdateRoom(data)
        except Exception as e:
            print(f"Update error: {e}")
            return {"error": str(e)}, 400

    def DeleteRoomByRID(self,rid):
        try:
            rid = int(rid)
            return self.Courses.DeleteRoomByRID(rid)
        except Exception as e:
            print(f"Delete error: {e}")
            return {"error": str(e)}, 400
        