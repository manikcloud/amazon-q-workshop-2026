# Python Calculator Web Application

## 🧮 Project Overview
A Flask-based web calculator with basic arithmetic and scientific functions, developed for the Amazon Q Workshop 2026.

## ✨ Features
- **Basic Operations**: Addition, subtraction, multiplication, division
- **Scientific Functions**: Sin, cos, square root
- **Error Handling**: Division by zero and invalid input protection
- **Web Interface**: Clean, responsive HTML/CSS design
- **Docker Support**: Containerized deployment ready

## 🚀 Quick Start

### Local Development
```bash
# Install dependencies
pip install flask

# Run the application
python app.py

# Access at http://localhost:5000
```

### Docker Deployment
```bash
# Build image
docker build -t python-calculator .

# Run container
docker run -p 5000:5000 python-calculator
```

## 📁 Project Structure
```
python-calculator/
├── app.py                    # Flask application
├── templates/               # HTML templates
├── calc_env/               # Virtual environment
├── Dockerfile              # Container configuration
├── requirements.txt        # Python dependencies
├── calculator-documentation.tex  # LaTeX documentation
└── README.md              # This file
```

## 🔧 Technical Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Deployment**: Docker, Python virtual environment

## 📊 Mathematical Operations

### Basic Operations
- Addition: `a + b`
- Subtraction: `a - b`
- Multiplication: `a × b`
- Division: `a ÷ b` (with zero-division protection)

### Scientific Functions
- Sine: `sin(x)`
- Cosine: `cos(x)`
- Square Root: `√x` (with negative number protection)

## 🧪 Testing
1. Start the application: `python app.py`
2. Open browser: `http://localhost:5000`
3. Test basic calculations: `2 + 3 = 5`
4. Test scientific functions: `sin(30°)`
5. Test error handling: `5 ÷ 0`

## 📚 Documentation
- **LaTeX Documentation**: `calculator-documentation.tex`
- **API Endpoints**: 
  - `GET /` - Calculator interface
  - `POST /calculate` - Perform calculations

## 🐳 Docker Configuration
```dockerfile
FROM python:3.11-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 🔗 Workshop Integration
This calculator is part of the Amazon Q Workshop 2026 hands-on demonstration, showcasing:
- AI-assisted development workflow
- Modern web application architecture
- Containerization best practices
- Documentation standards

## 📚 Additional Resources
For detailed Amazon Q setup and advanced configurations: [Amazon Q Setup Guide](https://github.com/manikcloud/amazon-q/tree/master)
