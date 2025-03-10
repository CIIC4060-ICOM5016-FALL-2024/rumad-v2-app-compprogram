from Models.MostClassPerSemesterYearModel import MostClassPerSemesterYearDAO

class MostClassPerSemesterYearController:
    def __init__(self):
        self.Course = MostClassPerSemesterYearDAO()
        
    def GET_Most_CLass_Per_Semester_Year(self,years,semester):
        
        try: 
            data = self.Course.GET_Most_CLass_Per_Semester_Year(years,semester)
            result = []
            for value in data:
                result.append(self.Course.Make_Dictionary(value)) 
            return result
        except:
            return {"error":f"Not a valid input: {years},{semester}"}
            
