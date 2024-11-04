from Models.SyllabusModel import SyllabusDAO

class SyllabusController:
    
    def __init__(self):#data should be a jsonfile from the user
        self.Courses = SyllabusDAO()

    def GetAllSyllabus(self):
        list = []
        data = self.Courses.GetAllSyllabus()
        for row in data:
            list.append(self.Courses.Make_Dictionary(row))
        return list
    
    def GetSyllabusByCHUNKID(self,chunkid):
        try:
            chunkid = int(chunkid)
            if chunkid < 0:
                return {"error": "Syllabus ID must be greater or equal to 0"}, 400
            data = self.Courses.GetSyllabusByCHUNKID(chunkid)
            return self.Courses.Make_Dictionary(data)
        except Exception as e:
            return {"error": f"This is not a valid chunkid: {chunkid}"}
    
    def InsertSyllabus(self,data):
        try:
            return self.Courses.InsertSyllabus(data)
        except Exception as e:
            print(f"Insertion error: {e}")
            return {"error": str(e)}, 400

    def UpdateSyllabus(self,data):
        try:
            return self.Courses.UpdateSyllabus(data)
        except Exception as e:
            print(f"Update error: {e}")
            return {"error": str(e)}, 400

    def DeleteSyllabusByCHUNKID(self,chunkid):
        try:
            chunkid = int(chunkid)
            return self.Courses.DeleteSyllabusByCHUNKID(chunkid)
        except Exception as e:
            print(f"Delete error: {e}")
            return {"error": str(e)}, 400
        