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
- 
- <img width="1397" height="980" alt="image" src="https://github.com/user-attachments/assets/a26f8e2e-604b-41fa-b6f8-4d420affca0e" />


## 🚀 How to Run Locally

### Option 1: Using Docker (Recommended)
```bash
# Navigate to calculator directory
cd 03-hands-on-demo/python-calculator

# Build the Docker image
docker build -t python-calculator .

# Run the container
docker run -p 5000:5000 python-calculator

# Access at: http://localhost:5000
```

### Option 2: Direct Python (if Docker unavailable)
```bash
# Navigate to calculator directory
cd 03-hands-on-demo/python-calculator

# Install Flask (choose one method):

# Method A: Using virtual environment (recommended)
python3 -m venv calc_env
source calc_env/bin/activate  # On Windows: calc_env\Scripts\activate
pip install flask
python app.py

# Method B: System-wide install (if allowed)
pip3 install flask
python3 app.py

# Method C: Break system packages (last resort)
pip3 install --break-system-packages flask
python3 app.py

# Access at: http://localhost:5000
```

### Option 3: Using pipx (Alternative)
```bash
# Install pipx if not available
brew install pipx  # On macOS
# or
sudo apt install pipx  # On Ubuntu

# Run with pipx
pipx run flask --app app.py run --host=0.0.0.0 --port=5000
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

## 🧪 Testing Examples
```
Basic: 2 + 3 * 4 = 14
Advanced: sqrt(16) + sin(0) = 4.0
Power: 2^3 = 8
Parentheses: (5 + 3) * 2 = 16
```

## 🐳 Why Docker?
- **No Virtual Environment Needed** - Container provides isolation
- **Consistent Environment** - Same behavior everywhere
- **Easy Deployment** - Single command to run
- **Lightweight** - Alpine Linux base (< 50MB)

---
**Generated for Amazon Q Workshop Demo - Lightweight & Beautiful Calculator**
