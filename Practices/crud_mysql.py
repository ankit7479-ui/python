from pdb import main

import mysql.connector
from mysql.connector import Error

class CRUDOperation:
    def __init__(self, host='localhost', database='crud_demo', user='root', password=''):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None
        
    def connect(self):
        """Establish database connection"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print(f"Connected to MySQL database '{self.database}'")
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
    def create_table(self):
        """CREATE:Create table structure"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                age INT,
                grade VARCHAR(10),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.connection.commit()
    def create_student(self,name,email,age,grade):
        """CREATE: Insert a new student record"""
        try:
            self.cursor.execute('''
                INSERT INTO students (name, email, age, grade) 
                VALUES (%s, %s, %s, %s)
            ''', (name, email, age, grade))
            self.connection.commit()
            print(f"Student '{name}' created successfully.")
        except Error as e:
            print(f"Error creating student: {e}")
        return None
    
    def get_all_students(self):
        """READ: Retrieve all student records"""
        self.cursor.execute('SELECT * FROM students')
        students = self.cursor.fetchall()
        return students
    
    def get_student_by_id(self, student_id):
        """READ: Retrieve a student record by ID"""
        self.cursor.execute('SELECT * FROM students WHERE id = %s', (student_id,))
        student = self.cursor.fetchone()
        return student
    def update_student(self,student_id,name=None,email=None,age=None,grade=None):
        """UPDATE: Update a student record by ID"""
        fields = []
        values = []
        
        if name:
            fields.append("name = %s")
            values.append(name)
        if email:
            fields.append("email = %s")
            values.append(email)
            if age:
                fields.append("age = %s")
                values.append(age)
            if grade:
                fields.append("grade = %s")
                values.append(grade)
        values.append(student_id)
        sql = f"UPDATE students SET {', '.join(fields)} WHERE id = %s"
        try:
            self.cursor.execute(sql, tuple(values))
            self.connection.commit()
            print(f"Student with ID {student_id} updated successfully.")
        except Error as e:
            print(f"Error updating student: {e}")
            
    def delete_student(self, student_id):
        """DELETE: Delete a student record by ID"""
        try:
            self.cursor.execute('DELETE FROM students WHERE id = %s', (student_id,))
            self.connection.commit()
            print(f"Student with ID {student_id} deleted successfully.")
        except Error as e:
            print(f"Error deleting student: {e}")
            
    def disconnect(self):
        """Close database connection"""
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("MySQL connection closed.")
            
if __name__ == "__main__":
    main()        
            
            