from Models.MeetingModel import MeetingDAO
from datetime import time, datetime, timedelta
# Query: Top 5 meetings with the most sections


class MeetingController:
    
    def __init__(self):#data should be a jsonfile from the user
        self.Courses = MeetingDAO()

    def GetAllMeetings(self):
        list = []
        data = self.Courses.getAllMeetings()
        for row in data:
            list.append(self.Courses.Make_Dictionary(row))
        return list
    
    def GetMeetingByMID(self,mid):
        try:
            mid = int(mid)
            if mid < 0:
                return {"error": "Meeting ID must be greater or equal to 0"}, 400
            data = self.Courses.GetMeetingByMID(mid)
            return self.Courses.Make_Dictionary(data)
        except Exception as e:
            return {"error": f"This is not a valid mid: {mid}"}
    
    def InsertMeeting(self,data):
        starttime = datetime.strptime(data["starttime"], "%H:%M:%S")
        endtime = datetime.strptime(data["endtime"], "%H:%M:%S")
        time_diff_MJ = timedelta(hours=1, minutes=15)
        time_diff_LMV = timedelta(hours=0, minutes=50)
        data["starttime"] = datetime.strptime(data["starttime"], "%H:%M:%S").time()
        data["endtime"] = datetime.strptime(data["endtime"], "%H:%M:%S").time()
        print(endtime-starttime)
         
        try:
            # checks if the days are valid 
            if (data["cdays"] != "LMV") and (data["cdays"] != "MJ"):
                return {"error": f"This meeting not being held in a valid day"}, 400
            
            # checks if the class being inserted is being held before 7:30am
            elif (data["starttime"] < time(7,30)) or (data["endtime"] <= time(7,30)) :
                return {"error": f"No meeting can be held before 7:30am"}, 400
            
             # checks the time difference in days for MJ are valid
            elif((endtime-starttime) != time_diff_MJ) and (data["cdays"] == "MJ"):
                return {"error": f"The meeting does not last for 1:15 hours"}, 400
            
            elif((endtime-starttime) != time_diff_LMV) and (data["cdays"] == "LMV"):
                return {"error": f"The meeting does not last for 50 minutes"}, 400
            
            # checks the meeting is being held during universal hour
            elif ((time(10,00) <= data["starttime"] <= time(11,59)) and data["cdays"] == "MJ") or ((time(10,00) < data["endtime"] <= time(11,59)) and data["cdays"] == "MJ"):
                return {"error": f"No meeting can be held during universal hour"}, 400  

            elif (data["starttime"] >= time(19,45)) or (data["endtime"] > time(19,45)):
                return {"error": f"Meetings cannot be held after 7:45pm"}, 400 
            
            return self.Courses.InsertMeeting(data)
        except Exception as e:
            print(f"Insertion error: {e}")
            return {"error": str(e)}, 400
        

    def UpdateMeeting(self,data):
        try:
            return self.Courses.UpdateMeeting(data)
        except Exception as e:
            print(f"Update error: {e}")
            return {"error": str(e)}, 400

    def DeleteMeetingByMID(self,mid):
        try:
            mid = int(mid)
            return self.Courses.DeleteMeetingByMID(mid)
        except Exception as e:
            print(f"Delete error: {e}")
            return {"error": str(e)}, 400
        