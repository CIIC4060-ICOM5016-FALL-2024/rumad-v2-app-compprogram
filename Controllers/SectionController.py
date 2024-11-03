from Models.SectionModel import SectionDAO

class SectionController:
    
    def __init__(self):#data should be a jsonfile from the user
        self.Courses = SectionDAO()

    def GetAllSections(self):
        list = []
        data = self.Courses.getAllSections()
        for row in data:
            list.append(self.Courses.Make_Dictionary(row))
        return list
    
    def GetSectionBySID(self,sid):
        try:
            sid = int(sid)
            if sid < 0:
                return {"error": "Section ID must be greater or equal to 0"}, 400
            data = self.Courses.GetSectionBySID(sid)
            return self.Courses.Make_Dictionary(data)
        except Exception as e:
            return {"error": f"This is not a valid sid: {sid}"}
    
    def InsertSection(self,data):
        try:
            return self.Courses.InsertSection(data)
        except Exception as e:
            print(f"Insertion error: {e}")
            return {"error": str(e)}, 400

    def UpdateSection(self,data):
        try:
            return self.Courses.UpdateSection(data)
        except Exception as e:
            print(f"Update error: {e}")
            return {"error": str(e)}, 400

    def DeleteSectionBySID(self,sid):
        try:
            sid = int(sid)
            return self.Courses.DeleteSectionBySID(sid)
        except Exception as e:
            print(f"Delete error: {e}")
            return {"error": str(e)}, 400
        