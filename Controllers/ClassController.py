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
        data = self.Courses.GetClassByCID(cid)
        result = self.Courses.Make_Dictionary(data)
        return result
    
    def InsertClass(self,data):
        return self.Courses.InsertClass(data)

    def UpdateClass(self,data):
        return self.Courses.UpdateClass(data)

