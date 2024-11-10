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
            return {"error": f"This is not a valid sid: {sid}"}, 400
    
    def InsertSection(self,data):
        try:
            roomid = int(data["roomid"])
            if (roomid < 0):
                return {"error": f"Invalid roomid {roomid} is below 0. roomid cannot be a negative number."}, 400    
        except ValueError:
            return {"error": f"Invalid roomid: {data['roomid']} is not a number"}, 400
        
        try:
            cid = int(data["cid"])
            if (cid < 0):
                return {"error": f"Invalid cid {cid} is below 0. cid cannot be a negative number."}, 400    
        except ValueError:
            return {"error": f"Invalid cid: {data['cid']} is not a number"}, 400
        
        try:
            mid = int(data["mid"])
            if (mid < 0):
                return {"error": f"Invalid mid {mid} is below 0. mid cannot be a negative number."}, 400                
        except ValueError:
            return {"error": f"Invalid mid: {data['mid']} is not a number"}, 400
        
        if (data["semester"] != "Fall") and (data["semester"] != "Spring") and (data["semester"] != "V1") and (data["semester"] != "V2"):
            return {"error": f"Invalid semester: {data['semester']} is not permitted. Please select Fall, Spring, V1, or V2. "}, 400       
        
        try:
            years = int(data["years"])
            if (years < 0):
                return {"error": f"Invalid year: the year you gave {years} is below 0. Years cannot be a negative number."}, 400
            
            elif (years < 2000):   
                return {"error": f"Invalid year: the year cannot before the 2000s, and the year you selected was {years}"}, 400        
        except ValueError:
            return {"error": f"Invalid year: {data['years']} is not a number"}, 400
        
        try:
            capacity = int(data["capacity"])
            if (capacity < 1):
                return {"error": f"Invalid capacity: capacity must be at least 1."}, 400               
        except ValueError:
            return {"error": f"Invalid capacity: {data['capacity']} is not a number"}, 400        

        try:
            return self.Courses.InsertSection(data)
        except Exception as e:
            print(f"Insertion error: {e}")
            return {"error": str(e)}, 400

    def UpdateSection(self,sid,data):
        try:
            sid = int(sid)
            if (sid < 0):
                return {"error": f"Invalid sid: {sid} is below 0. sid cannot be a negative number."}, 400    
        except ValueError:
            return {"error": f"Invalid sid: {sid} is not a number"}, 400
        
        try:
            roomid = int(data["roomid"])
            if (roomid < 0):
                return {"error": f"Invalid roomid {roomid} is below 0. roomid cannot be a negative number."}, 400    
        except ValueError:
            return {"error": f"Invalid roomid: {data['roomid']} is not a number"}, 400
        
        try:
            cid = int(data["cid"])
            if (cid < 0):
                return {"error": f"Invalid cid {cid} is below 0. cid cannot be a negative number."}, 400    
        except ValueError:
            return {"error": f"Invalid cid: {data['cid']} is not a number"}, 400
        
        try:
            mid = int(data["mid"])
            if (mid < 0):
                return {"error": f"Invalid mid {mid} is below 0. mid cannot be a negative number."}, 400                
        except ValueError:
            return {"error": f"Invalid mid: {data['mid']} is not a number"}, 400
        
        if (data["semester"] != "Fall") and (data["semester"] != "Spring") and (data["semester"] != "V1") and (data["semester"] != "V2"):
            return {"error": f"Invalid semester: {data['semester']} is not permitted. Please select Fall, Spring, V1, or V2."}, 400       
        
        try:
            years = int(data["years"])
            if (years < 0):
                return {"error": f"Invalid year: the year you gave {years} is below 0. Years cannot be a negative number."}, 400
            
            elif (years < 2000):   
                return {"error": f"Invalid year: the year cannot before the 2000s, and the year you selected was {years}"}, 400               
        except ValueError:
            return {"error": f"Invalid years: {data['years']} is not a number"}, 400
        
        try:
            capacity = int(data["capacity"])
            if (capacity < 1):
                return {"error": f"Invalid capacity: capacity must be at least 1."}, 400               
        except ValueError:
            return {"error": f"Invalid capacity: {data['capacity']} is not a number"}, 400        

        try:
            return self.Courses.UpdateSection(sid,data)
        except Exception as e:
            print(f"Update error: {e}")
            return {"error": str(e)}, 400

    def DeleteSectionBySID(self,sid):
        try:
            sid = int(sid)
        except ValueError:
            return {"error": f"Invalid type for id: {sid} is not a number"}, 400
        if (sid < 0):
            return {"error": f"Invalid id {sid} is below 0. Id cannot be a negative number."}, 400  
        
        try:
            return self.Courses.DeleteSectionBySID(sid)
        except Exception as e:
            print(f"Delete error: {e}")
            return {"error": str(e)}, 400
        