from config import *

# Query: Top 3 classes that appears the most as prerequisite to other classes.
class MostPrequisiteDao:
    def __init__(self):
        self.connection = psycopg2.connect(**db_params)
        self.cursor = self.connection.cursor()
    def GET_TOP_PREQUISITE(self):
        query = """SELECT reqid, class.cdesc, count(*) AS class_count
            FROM requisite 
            INNER JOIN class 
            ON reqid = class.cid 
            WHERE cdesc <> 'None' 
            GROUP BY reqid, class.cdesc 
            ORDER BY class_count DESC 
            LIMIT 3;"""
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
    def Make_Dictionary(self,data):
        result = {}
        result["requid"] = data[0]
        result["cdesc"] = data[1]
        result["total"] = data[2]
        return result

  
