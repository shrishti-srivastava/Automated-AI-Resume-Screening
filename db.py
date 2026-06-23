import mysql.connector

class Database:

    def __init__(self):

        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="ats_resume_db"
        )

        self.cursor = self.conn.cursor()

    def save_candidate(
            self,
            candidate
    ):

        query = """
        INSERT INTO candidates
        (
        name,
        email,
        score
        )
        VALUES(%s,%s,%s)
        """

        self.cursor.execute(
            query,
            (
                candidate.name,
                candidate.email,
                candidate.score
            )
        )

        self.conn.commit()

        return self.cursor.lastrowid
    
    def save_skills(
            self,
            candidate_id,
            skills
    ):
        
        for skill in skills:

            self.cursor.execute(
            """
            INSERT INTO candidate_skill
            (
            candidate_id,
            skill_name
            )
            VALUES(%s,%s)
            """,
            (
             candidate_id,
             skill   
            )
            )

        self.conn.commit()    

    
    