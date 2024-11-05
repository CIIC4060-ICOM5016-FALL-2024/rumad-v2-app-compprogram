from Models.MostClassPerRoomModels import MostClassPerRoomDAO

class MostClassPerRoomController:
    def __init__(self):
        self.Course = MostClassPerRoomDAO()
        
    def GET_Most_Class_Per_Room(self,cid):
        try:
            cid = int(cid)
            if cid < 0:
                return {"error":f"Cid must be greater than 0, your's below: {cid}"}
            data = self.Course.GET_Most_Class_Per_Room(cid)
            result = []
            for value in data:
                result.append(self.Course.Make_Dictionary(value,cid)) 
            return result
        except:
            return {"error":f"Not a valid cid: {cid}"}