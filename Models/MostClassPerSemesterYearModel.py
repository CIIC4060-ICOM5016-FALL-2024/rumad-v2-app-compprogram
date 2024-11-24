from config import *

class MostClassPerSemesterYearDAO:
    def __init__(self):
        self.connection = psycopg2.connect(**db_params)
        self.cursor = self.connection.cursor()
        
    def GET_Most_CLass_Per_Semester_Year(self,years,semester):
        query = """SELECT CONCAT(class.cname , ' ',class.ccode),section.semester,section.years,cdesc,count(*) as Class_Count
                    FROM CLASS
                    INNER JOIN SECTION
                    ON SECTION.CID = CLASS.CID
                    WHERE section.years = %s and section.semester = %s
                    GROUP BY section.semester,class.ccode,class.cname,class.cdesc,section.years
                    ORDER BY Class_Count DESC
                    LIMIT 3;
                        """
        self.cursor.execute(query,(years,semester,))
        result = self.cursor.fetchall()
        if len(result) == 0:
            return Exception
        return result
    
    
    def Make_Dictionary(self,data):
        result = {}
        result["Class Name"] = data[0]
        result["semester"] = data[1]
        result["years"] = data[2]
        result["cdesc"] = data[3]
        result["Class Count"] = data[4]
        return result