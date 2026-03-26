from ast import main
import sqlite3

class CRUDOperation:
    def __init__(self,db_name ='crud_demo.db'):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        
    def connect(self):
        """Establish database connection"""
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        print(f"Connected to {self.db_name}")

    def create_table(self):
        """CREATE: Create table structure"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                age INTEGER,
                grade TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.connection.commit()
        
    def create_student(self,name,email,age,grade):
        """CREATE: Insert a new student record"""
        try:
            self.cursor.execute('''
                INSERT INTO students (name, email, age, grade) 
                VALUES (?, ?, ?, ?)
            ''', (name, email, age, grade))
            self.connection.commit()
            print(f"Student '{name}' created successfully.")
        except sqlite3.IntegrityError as e:
            print(f"Error creating student: {e}")
        return None
        
    def get_all_students(self):
        """READ: Retrieve all student records"""
        self.cursor.execute('SELECT * FROM students')
        students = self.cursor.fetchall()
        return students
       
    def get_student_by_id(self, student_id):
        """READ: Retrieve a student record by ID"""
        self.cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
        student = self.cursor.fetchone()
        return student

    def update_student(self,student_id,name=None,email=None,age=None,grade=None):
        """UPDATE: Update a student record by ID"""
        fields = []
        values = []
        
        if name:
            fields.append("name = ?")
            values.append(name)
        if email:
            fields.append("email = ?")
            values.append(email)
        if age:
            fields.append("age = ?")
            values.append(age)
        if grade:
            fields.append("grade = ?")
            values.append(grade)
            
        if fields:
            values.append(student_id)
            sql = f"UPDATE students SET {', '.join(fields)} WHERE id = ?"
            self.cursor.execute(sql, values)
            self.connection.commit()
            
            if self.cursor.rowcount > 0:
                print(f"✅ Student ID {student_id} updated successfully")
                return True
            else:
                print(f"❌ Student ID {student_id} not found")
                return False
    
    def delete_student(self, student_id):
        """DELETE: Delete a student record by ID"""
        self.cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
        self.connection.commit()
        
        if self.cursor.rowcount > 0:
            print(f"✅ Student ID {student_id} deleted successfully")
            return True
        else:
            print(f"❌ Student ID {student_id} not found")
            return False

    def disconnect(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()

if __name__ == "__main__":
    try:
        crud = CRUDOperation()
        crud.connect()
        crud.create_table()
        crud.create_student("Alice Johnson", "alice@email.com", 20, "A")
        crud.create_student("Bob Smith", "bob@email.com", 22, "B+")
        crud.create_student("Charlie Brown", "charlie@email.com", 21, "A-")
        crud.create_student("Diana Prince", "diana@email.com", 23, "A+")
        
        # Get all students
        students = crud.get_all_students()
        print("All students:")
        for student in students:
            print(student)
        
        # Get a student by ID
        student = crud.get_student_by_id(1)
        print("\nStudent with ID 1:")
        print(student)
        
        # Update a student record
        crud.update_student(2, age=23, grade="A")
        # Delete a student record
        crud.delete_student(3)
        
        # final read to show changes
        students = crud.get_all_students()
        print("\nAll students after update and delete:")
        for student in students:
            print(student)
    
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        crud.disconnect()
        
 
if __name__ == "__main__":
   main()       
      