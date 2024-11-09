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
            return {"error": f"This is not a valid mid: {mid}"}, 400
    
    def InsertMeeting(self,data):
        # eliminate the try-except later, it's not doing anything
        starttime = datetime.strptime(data["starttime"], "%H:%M:%S")
        endtime = datetime.strptime(data["endtime"], "%H:%M:%S")
        time_diff_MJ = timedelta(hours=1, minutes=15)
        time_diff_LWV = timedelta(hours=0, minutes=50)
        data["starttime"] = datetime.strptime(data["starttime"], "%H:%M:%S").time()
        data["endtime"] = datetime.strptime(data["endtime"], "%H:%M:%S").time()
        print(endtime-starttime)
         
        try:
            # checks if the days are valid 
            if (data["cdays"] != "LWV") and (data["cdays"] != "MJ"):
                return {"error": f"Invalid meeting day: {data['cdays']} is not permitted. Please select LWV or MJ."}, 400
            
            # checks if the class being inserted is being held before 7:30am
            elif (data["starttime"] < time(7,30)) or (data["endtime"] <= time(7,30)) :
                return {"error": f"Invalid meeting time: meeting cannot be scheduled before 7:30am"}, 400
            
             # checks the time difference in days for MJ are valid
            elif((endtime-starttime) != time_diff_MJ) and (data["cdays"] == "MJ"):
                return {"error": f"Invalid duration: your current duration is {endtime-starttime}. For MJ days, the meeting is must last for 01:15:00."}, 400
            
            elif((endtime-starttime) != time_diff_LWV) and (data["cdays"] == "LWV"):
                return {"error": f"Invalid duration: your current duration is {endtime-starttime}. For LWV days, the meeting is must last for 00:50:00."}, 400
            
            # checks the meeting is being held during universal hour
            elif ((time(10,00) <= data["starttime"] <= time(11,59)) and data["cdays"] == "MJ") or ((time(10,00) < data["endtime"] <= time(11,59)) and data["cdays"] == "MJ"):
                return {"error": f"Invalid meeting time: meeting cannot be scheduled during universal hour 10:00-11:59"}, 400  

            # checks if time is being scheduled after 7:45pm
            elif (data["starttime"] >= time(19,45)) or (data["endtime"] > time(19,45)):
                return {"error": f"Invalid meeting time: meeting cannot be scheduled after 7:45pm"}, 400
            
            return self.Courses.InsertMeeting(data)
        except Exception as e:
            print(f"Insertion error: {e}")
            return {"error": str(e)}, 400
        

    def UpdateMeeting(self,mid,data):
        starttime = datetime.strptime(data["starttime"], "%H:%M:%S")
        endtime = datetime.strptime(data["endtime"], "%H:%M:%S")
        time_diff_MJ = timedelta(hours=1, minutes=15)
        time_diff_LWV = timedelta(hours=0, minutes=50)
        data["starttime"] = datetime.strptime(data["starttime"], "%H:%M:%S").time()
        data["endtime"] = datetime.strptime(data["endtime"], "%H:%M:%S").time()
        try:
            try:
                mid = int(mid)
            except ValueError:
                return {"error": f"Invalid id: {mid} is not a number"}, 400
                
            # mid cannot be negative
            if (mid < 0):
                return {"error": f"Invalid id {mid} is below 0. Id cannot be a negative number."}, 400
            
            elif (data["cdays"] != "LWV") and (data["cdays"] != "MJ"):
                return {"error": f"Invalid meeting day: {data['cdays']} is not permitted. Please select LWV or MJ."}, 400
            
            # checks if the class being inserted is being held before 7:30am
            elif (data["starttime"] < time(7,30)) or (data["endtime"] <= time(7,30)) :
                return {"error": f"Invalid meeting time: meeting cannot be scheduled before 7:30am"}, 400
            
             # checks the time difference in days for MJ are valid
            elif((endtime-starttime) != time_diff_MJ) and (data["cdays"] == "MJ"):
                return {"error": f"Invalid duration: your current duration is {endtime-starttime}. For MJ days, the meeting is must last for 01:15:00."}, 400
            
            elif((endtime-starttime) != time_diff_LWV) and (data["cdays"] == "LWV"):
                return {"error": f"Invalid duration: your current duration is {endtime-starttime}. For LWV days, the meeting is must last for 00:50:00."}, 400
            
            # checks the meeting is being held during universal hour
            elif ((time(10,00) <= data["starttime"] <= time(11,59)) and data["cdays"] == "MJ") or ((time(10,00) < data["endtime"] <= time(11,59)) and data["cdays"] == "MJ"):
                return {"error": f"Invalid meeting time: meeting cannot be scheduled during universal hour 10:00-11:59"}, 400  

            # checks if time is being scheduled after 7:45pm
            elif (data["starttime"] >= time(19,45)) or (data["endtime"] > time(19,45)):
                return {"error": f"Invalid meeting time: meeting cannot be scheduled after 7:45pm"}, 400
            
            return self.Courses.UpdateMeeting(mid,data)
        except Exception as e:
            # Checks if the primary key exist
            print(f"Update error: {e}")
            return {"error": str(e)}, 400

    def DeleteMeetingByMID(self,mid):
        try: 
            try:
                mid = int(mid)
            except ValueError:
                return {"error": f"Invalid type for id: {mid} is not a number"}, 400
            if (mid < 0):
                return {"error": f"Invalid id {mid} is below 0. Id cannot be a negative number."}, 400

            return self.Courses.DeleteMeetingByMID(mid)
        except Exception as e:
            print(f"Delete error: {e}")
            return {"error": str(e)}, 400
        