# Python Calculator Web Application Documentation

**Amazon Q Workshop 2026**  
*Date: January 19, 2025*

## Introduction
This document describes the Python Calculator web application developed as part of the Amazon Q Workshop 2026 hands-on demonstration.

## Project Overview
The calculator is a Flask-based web application that provides:
- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Scientific functions (sin, cos, sqrt)
- Error handling for invalid operations
- Web-based user interface

## Technical Architecture

### Backend
- **Framework:** Flask (Python web framework)
- **Language:** Python 3.x
- **Template Engine:** Jinja2

### Frontend
- **HTML5** for structure
- **CSS3** for styling
- **JavaScript** for client-side interactions

## Mathematical Operations
The calculator supports the following operations:

### Basic Operations
- **Addition:** `a + b`
- **Subtraction:** `a - b`
- **Multiplication:** `a × b`
- **Division:** `a ÷ b` (where `b ≠ 0`)

### Scientific Functions
- **Sine:** `sin(x)`
- **Cosine:** `cos(x)`
- **Square Root:** `√x` (where `x ≥ 0`)

## Implementation

```python
from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Implementation details
    pass
```

## Deployment
The application can be deployed using:
- **Local development server:** `python app.py`
- **Docker container:** `docker build -t calculator .`
- **Cloud platforms** (AWS, Heroku, etc.)

## Testing
Access the application at: [http://localhost:5000](http://localhost:5000)

## Conclusion
This calculator demonstrates modern web development practices using Python Flask framework, providing both educational value and practical functionality.
