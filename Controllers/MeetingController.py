from Models.MeetingModel import MeetingDAO

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
        try:
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
        