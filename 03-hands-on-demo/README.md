# 03 - Hands-On Demo

## 🎯 Learning Objectives
- Live demonstration of Amazon Q capabilities
- Interactive coding session with real CS examples
- Q&A and troubleshooting

## 📚 Demo Activities

### 1. **Code Generation** - Create functions from descriptions

#### **Demo Prompt 1: Data Structures**
```
Create a Python class for a Binary Search Tree with insert, search, and inorder traversal methods. Include proper error handling and documentation.
```

#### **Demo Prompt 2: Algorithm Implementation**
```
Write a Python function to implement the merge sort algorithm. The function should take a list of integers and return a sorted list. Add time complexity comments.
```

#### **Demo Prompt 3: Database Operations**
```
Create a Python function using SQLite to manage a student database with operations to add student, get student by ID, and list all students with their grades.
```

### 2. **AWS Integration** - Generate AWS CLI commands

#### **Demo Prompt 4: Cloud Infrastructure**
```
Generate AWS CLI commands to create an EC2 instance suitable for hosting a web application for a computer science project. Include security group configuration.
```

#### **Demo Prompt 5: S3 Storage Setup**
```
Create AWS CLI commands to set up an S3 bucket for storing student project files with proper permissions and versioning enabled.
```

#### **Demo Prompt 6: Lambda Function**
```
Generate a simple AWS Lambda function in Python that processes student grade submissions and stores them in DynamoDB.
```

### 3. **Debugging Help** - Fix code issues with Q assistance

#### **Demo Prompt 7: Debug Algorithm**
```
Here's a broken quicksort implementation. Can you identify and fix the bugs?

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x = pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
```

#### **Demo Prompt 8: Fix Web Application**
```
This Flask route for student registration isn't working. Please debug and fix:

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    student = Student(name, email)
    db.session.add(student)
    return "Student registered"
```

### 4. **Documentation** - Auto-generate code comments

#### **Demo Prompt 9: Document Complex Algorithm**
```
Add comprehensive documentation to this graph traversal algorithm including docstrings, inline comments, and complexity analysis:

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited
```

#### **Demo Prompt 10: API Documentation**
```
Generate complete API documentation for this student management system endpoint including request/response examples and error codes.
```

## 🛠️ Live Examples for Faculty

### **Teaching Aid Prompts**

#### **Demo Prompt 11: Create Assignment**
```
Generate a programming assignment for data structures course: "Create a hash table implementation with collision handling using chaining. Include test cases and grading rubric."
```

#### **Demo Prompt 12: Explain Concept**
```
Explain the concept of Big O notation to undergraduate students with simple examples and visual analogies. Include practice problems.
```

#### **Demo Prompt 13: Code Review Template**
```
Create a code review checklist template for evaluating student programming assignments in object-oriented programming course.
```

### **Research & Development Prompts**

#### **Demo Prompt 14: Research Code**
```
Generate Python code to implement a basic machine learning model for predicting student performance based on assignment scores and attendance.
```

#### **Demo Prompt 15: Data Analysis**
```
Create a Python script to analyze student grade distributions and generate statistical reports with visualizations using matplotlib.
```

## 🎓 Interactive Session Flow

1. **Start with simple prompts** (Prompts 1-3)
2. **Progress to AWS integration** (Prompts 4-6)
3. **Demonstrate debugging capabilities** (Prompts 7-8)
4. **Show documentation features** (Prompts 9-10)
5. **Faculty-specific examples** (Prompts 11-15)
6. **Open Q&A with custom prompts**

## 💡 Tips for Effective Prompts
- Be specific about requirements
- Include context (CS course, student level)
- Ask for explanations and comments
- Request error handling and best practices
- Specify output format when needed

---
[← Previous: Setup](../02-setup-installation/README.md) | [Back to Main](../README.md) | [Next: Exercise →](../04-practical-exercise/README.md)
