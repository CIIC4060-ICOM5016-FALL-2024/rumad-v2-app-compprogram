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
            #Cast them into integer to verify if it is a number, if not throw the error for not valid input
            classid = int(classid)
            reqid = int(reqid)
            #The class id must be greater than 0 if not throw the Primary key greater than 0 error
            if classid < 0 or reqid < 0:
                return {"error": f"Requisite PrimaryKey must be greater or equal to 0 and your is: ({classid},{reqid})"}, 400
            data = self.Courses.GetRequisiteByPrimaryKey(classid,reqid)
            # Once if found the correct data, can be make into a dictionary to answer the get request
            return self.Courses.Make_Dictionary(data)
        except Exception as e:
            try:
                #once again try to make them integer to indentify the type of error it it is an primar key not found 
                # or a varchar instead of a integer
                int(classid)
                int(reqid)
                return {"error": f"This Primary key was not found: ({classid},{reqid})"}, 400
            except:
                return {"error": f"This is not a valid PrimaryKey: ({classid},{reqid})"}, 400
    def InsertRequisite(self,data):
        try:
            #The requid must be true or false, other stuff will be considered a bad input
            if (bool(data["prereq"]) != True and bool(data["prereq"]) != False):
                return {"error":f"The reqid must be True or False and yours is: {data['prereq']}"}, 400
            #Verify if the data is an integer, if is not: is consider a bad input
            int(data["reqid"])
            int(data["classid"])
            return self.Courses.InsertRequisite(data)
        except Exception as e:
            try:
                #once again try to make them integer to indentify the type of error it it is an primar key not found 
                # or a varchar instead of a integer
                int(data["classid"])
                int(data["reqid"])
                return {"error": str(e)}, 400
            except:
                return {"error": f"The id's have to be integers and yours are: classid: {data['classid']} , reqid: {data['reqid']}"}, 400



    def UpdateRequisite(self,classid,reqid,data):
        try:
            #The requid must be true or false, other stuff will be considered a bad input
            if (bool(data["prereq"]) != True and bool(data["prereq"]) != False):
                return {"error":f"The reqid must be True or False and yours is: {data['prereq']}"}, 400
            #Verify if the data is an integer, if is not: is consider a bad input
            reqid = int(reqid)
            classid = int(classid)
            return self.Courses.UpdateRequisite(classid,reqid,data)
        except Exception as e:
            try:
                #once again try to make them integer to indentify the type of error it it is an primar key not found 
                # or a varchar instead of a integer
                classid = int(classid)
                reqid = int(reqid)
                return {"error": str(e)}, 400
            except:
                return {"error": f"The id's have to be integers and yours are: classid: {classid} , reqid: {reqid}"}, 400

    def DeleteRequisiteByPrimaryKey(self,classid,reqid):
        try:
            #Verify if it is an integer: to throw error of invalid input
            classid = int(classid)
            reqid = int(reqid)
            return self.Courses.DeleteRequisiteByPrimaryKey(classid,reqid)
        except Exception as e:
            try:
                classid = int(classid)
                reqid  = int(reqid)
                return {"error": str(e)}, 400
            except:
                return {"error": f"The id's have to be integers and yours are: classid: {classid} , reqid: {reqid}"}, 400

        