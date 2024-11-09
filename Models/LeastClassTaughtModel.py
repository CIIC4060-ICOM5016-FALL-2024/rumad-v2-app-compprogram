from config import *

# Query:Top 3 classes that were offered the least. 
class LeastClassTaughtDao:
    def __init__(self):
        self.connection = psycopg2.connect(**db_params)
        self.cursor = self.connection.cursor()


    def GET_LEAST_CLASS(self):
        query = """SELECT class.cid, class.cdesc, count(*) as class_count
        FROM class
        INNER JOIN section
        ON section.cid = class.cid
        WHERE cdesc <> 'None'
        GROUP BY class.cid, class.cdesc
        ORDER BY class_count ASC
        LIMIT 3"""
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
    
    
    def Make_Dictionary(self,data):
        result = {}
        result["cid"] = data[0]
        result["cdesc"] = data[1]
        result["total"] = data[2]
        return result

  
