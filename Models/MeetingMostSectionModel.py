from config import *

# Query: Top 5 meetings with the most sections

class MeetingMostSectionDao():
    def __init__(self):
      self.connection = psycopg2.connect(**db_params)
      self.cursor = self.connection.cursor()


    def GET_MEETING_WITH_MOST_SECTION(self):
      query = "SELECT mid, count(*) as meeting_number FROM section GROUP BY mid ORDER BY meeting_number DESC LIMIT 5"
      self.cursor.execute(query)
      result = self.cursor.fetchall()
      return result
    
    
    def Make_Dictionary(self,data):
      result = {}
      result["mid"] = data[0]
      result["total_sections"] = data[1]
      return result