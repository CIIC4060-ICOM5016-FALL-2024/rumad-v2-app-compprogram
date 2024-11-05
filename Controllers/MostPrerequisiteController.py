from Models.MostPrerequisiteModel import MostPrerequisiteDao

# Query: Top 3 classes that appears the most as prerequisite to other classes.
class MostPrerequisiteController:
    def __init__(self):
        self.DAO = MostPrerequisiteDao()
    

    def GET_TOP_PREREQUISITE(self):
        list = []
        data = self.DAO.GET_TOP_PREREQUISITE()
        for row in data:
            list.append(self.DAO.Make_Dictionary(row))
        return list

