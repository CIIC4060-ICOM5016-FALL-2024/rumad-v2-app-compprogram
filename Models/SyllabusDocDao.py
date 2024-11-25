from config import * 


class SyllabusDocDAO:
    def __init__(self):
        self.connection = psycopg2.connect(**db_params)#Connecting to the database;
        self.cursor = self.connection.cursor()

    def insertFragment(self, did, content, embedding):
        cursor = self.conn.cursor()
        query = "insert into fragments(did, content, embedding) values (%s, %s, %s) returning fid"
        cursor.execute(query, (did, content, embedding,))
        fid = cursor.fetchone()[0]
        self.conn.commit()
        return fid

    def getFragments(self,emb):
        cursor = self.conn.cursor()
        query = "select did, fid, embedding <=> %s as distance, content from fragments order by distance limit 30"
        cursor.execute(query, (emb,))
        result = []
        for row in cursor:
            result.append(row)
        return result