import sqlite3
import os

# Create database connection
def create_database():
    '''Create database and tables'''
    # Remove existing database if it exists (for clean setup)
    if os.path.exists('student_database.db'):
        os.remove('student_database.db')
    
    # Connect to SQLite database (creates file if doesn't exist)
    conn = sqlite3.connect('student_database.db')
    cursor = conn.cursor()
    
    # Create students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT UNIQUE NOT NULL,
            major TEXT NOT NULL,
            gpa REAL DEFAULT 0.0
        )
    ''')
    
    # Create courses table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            course_id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT NOT NULL,
            instructor TEXT NOT NULL,
            credits INTEGER NOT NULL,
            semester TEXT NOT NULL
        )
    ''')
    
    # Create enrollments table (junction table)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS enrollments (
            enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            course_id INTEGER,
            grade TEXT DEFAULT 'N/A',
            enrollment_date DATE DEFAULT CURRENT_DATE,
            FOREIGN KEY (student_id) REFERENCES students (id),
            FOREIGN KEY (course_id) REFERENCES courses (course_id)
        )
    ''')
    
    # Insert sample students
    students_data = [
        ('張小明', 20, 'ming@example.com', 'Computer Science', 3.8),
        ('李小華', 21, 'hua@example.com', 'Mathematics', 3.6),
        ('王小美', 19, 'mei@example.com', 'Physics', 3.9),
        ('陳小強', 22, 'qiang@example.com', 'Engineering', 3.5),
        ('林小芳', 20, 'fang@example.com', 'Biology', 3.7)
    ]
    
    cursor.executemany('''
        INSERT INTO students (name, age, email, major, gpa)
        VALUES (?, ?, ?, ?, ?)
    ''', students_data)
    
    # Insert sample courses
    courses_data = [
        ('Python Programming', 'Prof. Smith', 3, '2024 Fall'),
        ('Database Systems', 'Prof. Johnson', 4, '2024 Fall'),
        ('Data Structures', 'Prof. Brown', 3, '2024 Spring'),
        ('Web Development', 'Prof. Davis', 3, '2024 Fall'),
        ('Machine Learning', 'Prof. Wilson', 4, '2024 Spring')
    ]
    
    cursor.executemany('''
        INSERT INTO courses (course_name, instructor, credits, semester)
        VALUES (?, ?, ?, ?)
    ''', courses_data)
    
    # Insert sample enrollments
    enrollments_data = [
        (1, 1, 'A'),    # 張小明 enrolled in Python Programming
        (1, 2, 'B+'),   # 張小明 enrolled in Database Systems
        (2, 1, 'A-'),   # 李小華 enrolled in Python Programming
        (2, 3, 'B'),    # 李小華 enrolled in Data Structures
        (3, 1, 'A+'),   # 王小美 enrolled in Python Programming
        (3, 4, 'A'),    # 王小美 enrolled in Web Development
        (4, 2, 'B-'),   # 陳小強 enrolled in Database Systems
        (4, 5, 'C+'),   # 陳小強 enrolled in Machine Learning
        (5, 3, 'A-'),   # 林小芳 enrolled in Data Structures
        (5, 4, 'B+')    # 林小芳 enrolled in Web Development
    ]
    
    cursor.executemany('''
        INSERT INTO enrollments (student_id, course_id, grade)
        VALUES (?, ?, ?)
    ''', enrollments_data)
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    
    print("Database 'student_database.db' created successfully!")
    print("Tables created: students, courses, enrollments")
    print("Sample data inserted successfully!")

if __name__ == "__main__":
    create_database()