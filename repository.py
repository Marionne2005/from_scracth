from database import Database
from models import Student

class Operations():
    def __init__(self):
        self.db=Database()
        self.conn = self.db.conn
        self.cursor = self.conn.cursor()
        
    def create_student(self, student):
      self.cursor.execute('''
        INSERT INTO students (name, email, gpa, program) 
        VALUES (?, ?, ?, ?)
      ''', (student.get_name(), student.get_email(), student.get_gpa(), student.get_program()))
      self.conn.commit()
      return self.cursor.lastrowid # Return the ID of the newly created student

    def get_all_students(self):
        self.cursor.execute('SELECT * FROM students')
        rows = self.cursor.fetchall()
        return [Student(row[1], row[2], row[3], row[4]) for row in rows]    
    
    def get_student_by_id(self, student_id):
        self.cursor.execute('SELECT * FROM students WHERE student_id = ?', (student_id,))
        row = self.cursor.fetchone()
        if row:
            return Student(row[1], row[2], row[3], row[4])
        return None
    
    def update_student(self, student_id, student):
        self.cursor.execute(''' 
            UPDATE students 
            SET name = ?, email = ?, gpa = ?, program = ?
            WHERE student_id = ?''', (student.get_name(), student.get_email(), student.get_gpa(), student.get_program(), student_id))
        self.conn.commit()

    def update_gpa(self, student_id, new_gpa):
        self.cursor.execute('UPDATE students SET gpa = ? WHERE student_id = ?', (new_gpa, student_id))
        self.conn.commit()    

    def delete_student(self, student_id):
        self.cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
        self.conn.commit()


    def search_by_name(self,name):
        self.cursor.execute('SELECT * FROM students WHERE name LIKE ?', ('%' + name + '%',))
        rows = self.cursor.fetchall()
        return [Student(row[1], row[2], row[3], row[4]) for row in rows]    
    
    """SQL injection happens when user input is directly concatenated into a SQL query string, 
    allowing an attacker to inject malicious SQL code that gets executed. Parameterized queries using ? 
    placeholders prevent this because the database treats the substituted 
    value strictly as data, never as executable SQL syntax, regardless of what characters it contains."""

    def get_average_gpa(self):
        self.cursor.execute('SELECT AVG(gpa) FROM students')
        avg_gpa = self.cursor.fetchone()[0]
        return avg_gpa if avg_gpa is not None else 0.0
    
    def close(self):
        self.conn.close()