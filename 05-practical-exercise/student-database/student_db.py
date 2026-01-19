import sqlite3
import os

class StudentDatabase:
    def __init__(self, db_name="students.db"):
        self.db_name = db_name
        self.init_database()
    
    def init_database(self):
        """Initialize the database and create students table"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                grade REAL DEFAULT 0.0
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def add_student(self, name, email, grade=0.0):
        """Add a new student to the database"""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO students (name, email, grade)
                VALUES (?, ?, ?)
            ''', (name, email, grade))
            
            conn.commit()
            student_id = cursor.lastrowid
            conn.close()
            
            print(f"Student added successfully with ID: {student_id}")
            return student_id
            
        except sqlite3.IntegrityError:
            print(f"Error: Email {email} already exists")
            return None
        except Exception as e:
            print(f"Error adding student: {e}")
            return None
    
    def get_student_by_id(self, student_id):
        """Get student information by ID"""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT id, name, email, grade FROM students WHERE id = ?
            ''', (student_id,))
            
            student = cursor.fetchone()
            conn.close()
            
            if student:
                return {
                    'id': student[0],
                    'name': student[1],
                    'email': student[2],
                    'grade': student[3]
                }
            else:
                print(f"No student found with ID: {student_id}")
                return None
                
        except Exception as e:
            print(f"Error retrieving student: {e}")
            return None
    
    def list_all_students(self):
        """List all students with their grades"""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT id, name, email, grade FROM students ORDER BY name
            ''')
            
            students = cursor.fetchall()
            conn.close()
            
            if students:
                print("\n=== All Students ===")
                print(f"{'ID':<5} {'Name':<20} {'Email':<25} {'Grade':<8}")
                print("-" * 60)
                
                student_list = []
                for student in students:
                    print(f"{student[0]:<5} {student[1]:<20} {student[2]:<25} {student[3]:<8}")
                    student_list.append({
                        'id': student[0],
                        'name': student[1],
                        'email': student[2],
                        'grade': student[3]
                    })
                
                return student_list
            else:
                print("No students found in database")
                return []
                
        except Exception as e:
            print(f"Error listing students: {e}")
            return []

# Example usage and testing
if __name__ == "__main__":
    # Create database instance
    db = StudentDatabase()
    
    print("=== Student Database Management System ===\n")
    
    # Add sample students
    print("1. Adding students...")
    db.add_student("Alice Johnson", "alice@university.edu", 85.5)
    db.add_student("Bob Smith", "bob@university.edu", 92.0)
    db.add_student("Carol Davis", "carol@university.edu", 78.3)
    
    # List all students
    print("\n2. Listing all students...")
    db.list_all_students()
    
    # Get specific student
    print("\n3. Getting student by ID...")
    student = db.get_student_by_id(2)
    if student:
        print(f"Found: {student['name']} - Grade: {student['grade']}")
    
    # Try to add duplicate email
    print("\n4. Testing duplicate email...")
    db.add_student("Alice Clone", "alice@university.edu", 90.0)
    
    print("\n=== Demo Complete ===")
