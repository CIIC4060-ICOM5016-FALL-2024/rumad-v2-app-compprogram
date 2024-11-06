from Models.RequisiteModel import RequisiteDAO

class RequisiteController:
    
    def __init__(self):#data should be a jsonfile from the user
        self.Courses = RequisiteDAO()

    def GetAllRequisites(self):
        list = []
        data = self.Courses.GetAllRequisites()
        for row in data:
            list.append(self.Courses.Make_Dictionary(row))
        return list
    
    def GetRequisiteByPrimaryKey(self,classid,reqid):
        try:
            if (data["reqid"] != True and data["reqid"] != False):
                return {"error":f"The reqid must be True or False and yours is: {data["reqid"]}"}
            classid = int(classid)
            reqid = int(reqid)
            if classid < 0 and reqid < 0:
                return {"error": "Requisite PrimaryKey must be greater or equal to 0"}, 400
            data = self.Courses.GetRequisiteByPrimaryKey(classid,reqid)
            return self.Courses.Make_Dictionary(data)
        except Exception as e:
            return {"error": f"This is not a valid PrimaryKey: ({classid},{reqid})"}
    
    def InsertRequisite(self,data):
        try:
            return self.Courses.InsertRequisite(data)
        except Exception as e:
            print(f"Insertion error: {e}")
            return {"error": str(e)}, 400

    def UpdateRequisite(self,data):
        try:
            return self.Courses.UpdateRequisite(data)
        except Exception as e:
            print(f"Update error: {e}")
            return {"error": str(e)}, 400

    def DeleteRequisiteByPrimaryKey(self,classid,reqid):
        try:
            classid = int(classid)
            reqid = int(reqid)
            return self.Courses.DeleteRequisiteByPrimaryKey(classid,reqid)
        except Exception as e:
            print(f"Delete error: {e}")
            return {"error": str(e)}, 400
        