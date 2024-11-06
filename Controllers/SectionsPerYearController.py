from Models.SectionsPerYearModel import SectionsPerYearDao

# Query: Total number of sections per year
class SectionsPerYearController:
    def __init__(self):
        self.DAO = SectionsPerYearDao()
    

    def GET_SECTIONS_PER_YEAR(self):
        list = []
        data = self.DAO.GET_SECTIONS_PER_YEAR()
        for row in data:
            list.append(self.DAO.Make_Dictionary(row))
        return list

