# File: calculator.py

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero.")

# Usage example:
# calc = Calculator()
# print(calc.multiply(2, 6))   # Output: 12
# print(calc.divide(10, 2))    # Output: 5.0
# print(calc.divide(10, 0))    # Raises ValueError: Cannot divide by zero.