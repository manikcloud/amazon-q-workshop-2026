# 🧮 Python Calculator - Web Application

## 🎯 Overview
A beautiful web-based Python calculator with advanced mathematical functions, built with Flask and containerized for easy deployment.

## ✨ Features
- **Beautiful UI** with gradient backgrounds and smooth animations
- **Basic Operations** - Addition, subtraction, multiplication, division
- **Advanced Functions** - Square root, power, trigonometric functions
- **Calculation History** - View and clear previous calculations
- **Keyboard Support** - Full keyboard navigation
- **Responsive Design** - Works on all devices
- **Lightweight Container** - Alpine Linux based Docker image

## 🚀 Quick Start

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

### Docker Container
```bash
# Build the image
docker build -t python-calculator .

# Run the container
docker run -p 5000:5000 python-calculator
```

## 🎨 UI Features
- **Gradient Backgrounds** - Modern visual design
- **Button Animations** - Hover and click effects
- **Error Handling** - Clear error messages
- **History Panel** - Track calculations
- **Mobile Responsive** - Touch-friendly interface

## 🔧 Technical Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Container**: Docker (Alpine Linux)
- **Math Functions**: Python math library

## 📱 Usage
1. **Basic Calculations**: Click numbers and operators
2. **Advanced Functions**: Use sqrt(), sin(), cos(), ^ for power
3. **Keyboard Support**: Type directly or use Enter for equals
4. **History**: View past calculations in the history panel
5. **Clear**: Use C button or Escape key

## 🧪 Testing
Access the calculator at: `http://localhost:5000`

**Test Cases:**
- Basic: `2 + 3 * 4`
- Advanced: `sqrt(16) + sin(0)`
- Power: `2^3`
- Parentheses: `(5 + 3) * 2`

---
**Generated for Amazon Q Workshop Demo - Lightweight & Beautiful Calculator**
