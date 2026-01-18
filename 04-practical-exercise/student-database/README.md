# Student Database Management System

## 🎯 Overview
A complete SQLite-based student database management system demonstrating CRUD operations, error handling, and proper database design.

## 📁 Files
- `student_db.py` - Main database class implementation
- `students.db` - SQLite database file (auto-created)

## 🛠️ Features
- **Add Student** - Insert new students with name, email, and grade
- **Get Student by ID** - Retrieve specific student information
- **List All Students** - Display all students in formatted table
- **Error Handling** - Duplicate email prevention and exception handling
- **Auto-initialization** - Database and table creation on first run

## 🚀 Usage

### Run the Demo
```bash
python3 student_db.py
```

### Use in Your Code
```python
from student_db import StudentDatabase

# Create database instance
db = StudentDatabase()

# Add students
student_id = db.add_student("John Doe", "john@university.edu", 88.5)

# Get student
student = db.get_student_by_id(student_id)

# List all students
all_students = db.list_all_students()
```

## 📊 Database Schema
```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    grade REAL DEFAULT 0.0
);
```

## ✅ Test Results
- ✅ Successfully adds students
- ✅ Prevents duplicate emails
- ✅ Retrieves students by ID
- ✅ Lists all students in formatted table
- ✅ Handles errors gracefully

---
[← Back to Exercise](../README.md)
