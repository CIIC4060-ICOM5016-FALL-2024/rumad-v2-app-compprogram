from Models.LeastClassTaughtModel import LeastClassTaughtDao

# Query: Top 3 classes that appears the most as prerequisite to other classes.
class LeastClassTaughtController:
    def __init__(self):
        self.DAO = LeastClassTaughtDao()
    

    def GET_LEAST_CLASS(self):
        list = []
        data = self.DAO.GET_LEAST_CLASS()
        for row in data:
            list.append(self.DAO.Make_Dictionary(row))
        return list

