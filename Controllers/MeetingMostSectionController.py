from Models.MeetingMostSectionModel import MeetingMostSectionDao


class MeetingMostSectionController:
    def __init__(self):
        self.DAO = MeetingMostSectionDao()

    
    def GET_MEETING_WITH_MOST_SECTION(self):
        list = []
        data = self.DAO.GET_MEETING_WITH_MOST_SECTION()
        for row in data:
            list.append(self.DAO.Make_Dictionary(row))
        return list