from Models.ClassModel import ClassDAO

class ClassController:
    
    def __init__(self):#data should be a jsonfile from the user
        self.Courses = ClassDAO()

    def GetAllClasses(self):
        list = []
        data = self.Courses.GetAllClasses()
        for row in data:
            list.append(self.Courses.Make_Dictionary(row))
        return list
    
    def GetClassByCID(self,cid):
        try:
            cid = int(cid)
            if cid < 2:
                return {"error": "Class ID must be greater than 1"}, 400
            data = self.Courses.GetClassByCID(cid)
            return self.Courses.Make_Dictionary(data)
        except Exception as e:
            return {"error": f"This is not a valid CID: {cid}"}, 400
    
    def InsertClass(self,data):
        try:

            if(data["cname"] != "CIIC") and (data["cname"] != "INSO"):
                return {"error": f"This is not valid cname: {data['cname']}. Please enter CIIC or INSO"}, 400
            
            elif(len(data["cname"]) != 4):
                return {"error": f"This is a not valid cname"}, 400
            
            try:
                ccode = int(data["ccode"])
                if(len(data["ccode"]) != 4 ): 
                    return {"error" : f"This is not a valid ccode: {data['ccode']}. Please enter a code with only 4 digits"}, 400
            except Exception as e:
                return {"error" : f"This is not a valid ccode: {data['ccode']}. The code can only have numbers"}, 400
            
            if(isinstance(int(data["cdesc"]), int)):
                return {"error" : f"This is not a valid cdesc: {data['cdesc']}. The cdesc needs to be a string"}, 400
            
            elif(data["term"] != "None") and (data["term"] != "First Semester") and (data["term"] != "Second Semester") and (data["term"] != "According to Demand") and (data["term"] != "First Semester, Second Semester"):
                return {"error" : f"This is not a valid term: {data['term']}. Please select First Semester, Second Semester, According to Demand or 'First Semester, Second Semester'"}, 400

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
        