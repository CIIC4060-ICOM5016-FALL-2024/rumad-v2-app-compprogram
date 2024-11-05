from Models.MostCapacityRoomsModels import MostCapacityRoomsDAO

class MostCapacityRoomsController:
    def __init__(self):
        self.Course = MostCapacityRoomsDAO()
        
    def GET_Most_Capacity_Rooms(self,building):
        if building == "Stefani" or building == "Monzon" or building == "Software" :
            data = self.Course.GET_Most_Capacity_Rooms(building)
            result = []
            for value in data:
                result.append(self.Course.Make_Dictionary(value)) 
            return result
        else:
            return {"error" : "Not a valid building: " + str(building)},400