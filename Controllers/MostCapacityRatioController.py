from Models.MostCapacityRatioModels import MostCapacityRatioDAO

class MostCapacityRatioController:
    def __init__(self):
        self.Course = MostCapacityRatioDAO()
        
    def GET_MOST_CAPACITY_RATIO(self,rid):
        try:
            rid = int(rid)
            if(rid < 0):
                return {"error":"This RID is below 0"}
            data = self.Course.GET_MOST_CAPACITY_RATIO(rid)
            result = []
            for value in data:
                result.append(self.Course.Make_Dictionary(value)) 
            return result
        except:
            return {"error ":"Not a valid rid: " + str(rid)}