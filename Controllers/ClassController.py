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
                return {"error": f"Invalid cname: {data['cname']}. Please enter CIIC or INSO"}, 400
            
            try:
                ccode = str(data["ccode"])  
                if(len(ccode) != 4 ): 
                    return {"error" : f"Invalid ccode: {data['ccode']}. Please enter a code with only 4 digits"}, 400
                int(ccode)
            except Exception as e:
                return {"error" : f"Invalid ccode: {data['ccode']}. The code can only have numbers"}, 400
            
            if (not type(data["cdesc"]) == str) or data["cdesc"].isdigit():
                return {"error": f"Invalid cdesc: {data['cdesc']}. The cdesc needs to be a string"}, 400

            if (data["term"]) not in ["None", "First Semester","Second Semester", "First Semester, Second Semester", "According to Demand"]:
                return {"error" : f"Invalid term: {data['term']}. Please select First Semester, Second Semester, According to Demand or 'First Semester, Second Semester'"}, 400
            
            if (data["years"]) not in ["None", "Every Year","Odd Years", "Even Years", "According to Demand"]:
                return {"error" : f"Invalid year: {data['years']}. Please pick None, Every Year, Even Years, Odd Years, According to Demand"}, 400
            
            try:
                cred = int(data["cred"])
                if not(0 <= cred <= 5):
                    return {"error": f"Invalid cred: {data['cred']}. Credits must be between 0 to 5"}, 400
            except ValueError: 
                return {"error" : f"Invalid cred: {data['cred']}. Credits must be an integer"}, 400
            
            
            if data['csyllabus'].isdigit():
                return {"error" : f"Invalid syllabus: {data['syllabus']}. Syllabus link cannot be purely numbers"}, 400
                
            return self.Courses.InsertClass(data)
        except Exception as e:
            return {"error": str(e)}, 400

    def UpdateClass(self,cid,data):
        try:
            try:
                cid = int(cid)
            except ValueError:
                return {"error": f"Invalid cid: {cid} is not a number"}, 400
            
            if(data["cname"] != "CIIC") and (data["cname"] != "INSO"):
                return {"error": f"Invalid cname: {data['cname']}. Please enter CIIC or INSO"}, 400
            
            try:
                ccode = str(data["ccode"])  
                if(len(ccode) != 4 ): 
                    return {"error" : f"Invalid ccode: {data['ccode']}. Please enter a code with only 4 digits"}, 400
                int(ccode)
            except Exception as e:
                return {"error" : f"Invalid ccode: {data['ccode']}. The code can only have numbers"}, 400
            
            if not type(data["cdesc"]) == str or data["cdesc"].isdigit():
                return {"error": f"Invalid cdesc: {data['cdesc']}. The cdesc needs to be a string"}, 400

            if (data["term"]) not in ["None", "First Semester","Second Semester", "First Semester, Second Semester", "According to Demand"]:
                return {"error" : f"Invalid term: {data['term']}. Please select First Semester, Second Semester, According to Demand or 'First Semester, Second Semester'"}, 400
            
            if (data["years"]) not in ["None", "Every Year","Odd Years", "Even Years", "According to Demand"]:
                return {"error" : f"Invalid year: {data['years']}. Please pick None, Every Year, Even Years, Odd Years, According to Demand"}, 400
            
            try:
                cred = int(data["cred"])
                if not(0 <= cred <= 5):
                    return {"error": f"Invalid cred: {data['cred']}. Credits must be between 0 to 5"}, 400
            except ValueError: 
                return {"error" : f"Invalid cred: {data['cred']}. Credits must be an integer"}, 400
            
            
            if not type(data['csyllabus']) == str or data['csyllabus'].isdigit():
                return {"error" : f"Invalid syllabus: {data['csyllabus']}. Syllabus link cannot be purely numbers"}, 400
            
            return self.Courses.UpdateClass(cid,data)
        except Exception as e:
            print(f"Update error: {e}")
            return {"error": str(e)}, 400

    def DeleteClassByCID(self,cid):
        try:
            cid = int(cid)
            if (cid < 2):
                return {"error": f"Invalid cid: {cid}. The cid must be greater than 1"}, 400
            return self.Courses.DeleteClassByCID(cid)
        except Exception as e:
            print(f"Delete error: {e}")
            return {"error": str(e)}, 400
        