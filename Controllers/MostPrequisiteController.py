from Models.MostPrequisiteModel import MostPrequisiteDao

# Query: Top 3 classes that appears the most as prerequisite to other classes.
class MostPrequisiteController:
    def __init__(self):
        self.DAO = MostPrequisiteDao()
    

    def GET_TOP_PREQUISITE(self):
        list = []
        data = self.DAO.GET_TOP_PREQUISITE()
        for row in data:
            list.append(self.DAO.Make_Dictionary(row))
        return list

