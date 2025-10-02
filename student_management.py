import sqlite3
from datetime import datetime

class StudentManagementSystem:
    def __init__(self, db_name='student_database.db'):
        '''Initialize the Student Management System'''
        self.db_name = db_name
        
    def connect_db(self):
        '''Create a database connection'''
        return sqlite3.connect(self.db_name)
    
    def add_student(self, name, age, email, major, gpa=0.0):
        '''Add a new student to the database'''
        try:
            conn = self.connect_db()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO students (name, age, email, major, gpa)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, age, email, major, gpa))
            
            conn.commit()
            student_id = cursor.lastrowid
            conn.close()
            
            print(f"Student '{name}' added successfully with ID: {student_id}")
            return student_id
            
        except sqlite3.IntegrityError as e:
            print(f"Error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
    
    def get_all_students(self):
        '''Retrieve all students from the database'''
        conn = self.connect_db()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM students ORDER BY name')
        students = cursor.fetchall()
        
        conn.close()
        return students
    
    def get_student_by_id(self, student_id):
        '''Get a specific student by ID'''
        conn = self.connect_db()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
        student = cursor.fetchone()
        
        conn.close()
        return student
    
    def update_student_gpa(self, student_id, new_gpa):
        '''Update a student's GPA'''
        try:
            conn = self.connect_db()
            cursor = conn.cursor()
            
            cursor.execute('''
                UPDATE students SET gpa = ? WHERE id = ?
            ''', (new_gpa, student_id))
            
            if cursor.rowcount > 0:
                conn.commit()
                print(f"Student ID {student_id} GPA updated to {new_gpa}")
                result = True
            else:
                print(f"No student found with ID {student_id}")
                result = False
                
            conn.close()
            return result
            
        except Exception as e:
            print(f"Error updating GPA: {e}")
            return False
    
    def get_students_by_major(self, major):
        '''Get all students in a specific major'''
        conn = self.connect_db()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM students WHERE major = ? ORDER BY gpa DESC
        ''', (major,))
        
        students = cursor.fetchall()
        conn.close()
        return students
    
    def get_course_enrollments(self, course_id):
        '''Get all students enrolled in a specific course'''
        conn = self.connect_db()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT s.id, s.name, s.major, e.grade
            FROM students s
            JOIN enrollments e ON s.id = e.student_id
            WHERE e.course_id = ?
            ORDER BY s.name
        ''', (course_id,))
        
        enrollments = cursor.fetchall()
        conn.close()
        return enrollments
    
    def get_student_courses(self, student_id):
        '''Get all courses for a specific student'''
        conn = self.connect_db()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT c.course_name, c.instructor, c.credits, e.grade
            FROM courses c
            JOIN enrollments e ON c.course_id = e.course_id
            WHERE e.student_id = ?
            ORDER BY c.course_name
        ''', (student_id,))
        
        courses = cursor.fetchall()
        conn.close()
        return courses
    
    def display_all_students(self):
        '''Display all students in formatted way'''
        students = self.get_all_students()
        
        if not students:
            print("No students found in database.")
            return
        
        print("\n=== ALL STUDENTS ===")
        print(f"{'ID':<4} {'Name':<15} {'Age':<4} {'Email':<25} {'Major':<20} {'GPA':<5}")
        print("-" * 80)
        
        for student in students:
            print(f"{student[0]:<4} {student[1]:<15} {student[2]:<4} {student[3]:<25} {student[4]:<20} {student[5]:<5}")
    
    def display_courses_by_student(self, student_id):
        '''Display all courses for a specific student'''
        student = self.get_student_by_id(student_id)
        if not student:
            print(f"No student found with ID {student_id}")
            return
        
        courses = self.get_student_courses(student_id)
        
        print(f"\n=== COURSES FOR {student[1]} (ID: {student_id}) ===")
        if not courses:
            print("No courses found for this student.")
            return
        
        print(f"{'Course Name':<25} {'Instructor':<15} {'Credits':<8} {'Grade':<6}")
        print("-" * 60)
        
        for course in courses:
            print(f"{course[0]:<25} {course[1]:<15} {course[2]:<8} {course[3]:<6}")

def main():
    '''Main function to demonstrate the Student Management System'''
    sms = StudentManagementSystem()
    
    print("=== Student Management System Demo ===\n")
    
    # Display all students
    sms.display_all_students()
    
    # Add a new student
    print("\n=== Adding New Student ===")
    new_student_id = sms.add_student("劉小傑", 21, "jie@example.com", "Computer Science", 3.4)
    
    # Update a student's GPA
    print("\n=== Updating Student GPA ===")
    sms.update_student_gpa(1, 3.9)
    
    # Display students by major
    print("\n=== Students in Computer Science Major ===")
    cs_students = sms.get_students_by_major("Computer Science")
    for student in cs_students:
        print(f"ID: {student[0]}, Name: {student[1]}, GPA: {student[5]}")
    
    # Display courses for a specific student
    sms.display_courses_by_student(1)
    
    # Display course enrollments
    print("\n=== Students Enrolled in Course ID 1 (Python Programming) ===")
    enrollments = sms.get_course_enrollments(1)
    for enrollment in enrollments:
        print(f"Student: {enrollment[1]}, Major: {enrollment[2]}, Grade: {enrollment[3]}")

if __name__ == "__main__":
    main()