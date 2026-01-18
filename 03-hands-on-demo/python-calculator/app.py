from flask import Flask, render_template, request, jsonify
import math
import re

app = Flask(__name__)

class Calculator:
    def __init__(self):
        self.history = []
    
    def evaluate(self, expression):
        try:
            # Replace common math functions
            expression = expression.replace('^', '**')
            expression = re.sub(r'(\d+)!', r'math.factorial(\1)', expression)
            
            # Safe evaluation with math functions
            allowed_names = {
                k: v for k, v in math.__dict__.items() if not k.startswith("__")
            }
            allowed_names.update({"abs": abs, "round": round})
            
            result = eval(expression, {"__builtins__": {}}, allowed_names)
            
            # Add to history
            self.history.append({"expression": expression, "result": result})
            if len(self.history) > 10:  # Keep only last 10 calculations
                self.history.pop(0)
            
            return {"success": True, "result": result}
        
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_history(self):
        return self.history
    
    def clear_history(self):
        self.history = []

calculator = Calculator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get('expression', '')
    
    result = calculator.evaluate(expression)
    return jsonify(result)

@app.route('/history')
def get_history():
    return jsonify(calculator.get_history())

@app.route('/clear-history', methods=['POST'])
def clear_history():
    calculator.clear_history()
    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
