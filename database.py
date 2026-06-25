import sqlite3

class Database:

    def __init__(self, db_name="students.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        self.cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                gpa REAL NOT NULL CHECK(gpa >= 0.0 AND gpa <= 4.0),
                program TEXT NOT NULL 
            )''')
        self.conn.commit()
    
    def close(self):
        self.conn.close()
    