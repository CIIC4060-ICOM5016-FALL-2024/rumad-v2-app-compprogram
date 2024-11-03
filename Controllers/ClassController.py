from Models.ClassModel import ClassDAO

class ClassController:
    
    def __init__(self):#data should be a jsonfile from the user
        self.Courses = ClassDAO()

    def GetAllClass(self):
        list = []
        data = self.Courses.getAllData()
        for row in data:
            list.append(self.Courses.Make_Dictionary(row))
        return list
    
    def GetClassByCID(self,cid):
        try:
            cid = int(cid)
            if cid < 2:
                return {"error": "Class ID must be greater than 1"}, 400
            data = self.Courses.GetClassByCID(cid)
            return data
        except Exception as e:
            return {"error": f"This is not a valid CID: {cid}"}
    
    def InsertClass(self,data):
        try:
            return self.Courses.InsertClass(data)
        except Exception as e:
            print(f"Insertion error: {e}")
            return {"error": str(e)}, 400

    def UpdateClass(self,data):
        try:
            return self.Courses.UpdateClass(data)
        except Exception as e:
            print(f"Update error: {e}")
            return {"error": str(e)}, 400

    def DeleteClassByCID(self,cid):
        try:
            cid = int(cid)
            return self.Courses.DeleteClassByCID(cid)
        except Exception as e:
            print(f"Delete error: {e}")
            return {"error": str(e)}, 400
        