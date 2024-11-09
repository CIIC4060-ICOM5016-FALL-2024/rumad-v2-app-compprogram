from config import *

# Query:Top 3 classes that were offered the least. 
class SectionsPerYearDao:
    def __init__(self):
        self.connection = psycopg2.connect(**db_params)
        self.cursor = self.connection.cursor()


    def GET_SECTIONS_PER_YEAR(self):
        query = """SELECT years, count(*) as sections_per_year
        FROM section
        GROUP BY years
        ORDER BY years"""
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
    
    
    def Make_Dictionary(self,data):
        result = {}
        result["years"] = data[0]
        result["sections_per_year"] = data[1]
        return result

  
