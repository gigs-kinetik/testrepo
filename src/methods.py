
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, value):
        """Adds a number to the current result."""
        self.result += value
        return self.result

    def subtract(self, value):
        """Subtracts a number from the current result."""
        self.result -= value
        return self.result

    def multiply(self, value):
        """Multiplies the current result by a number."""
        self.result *= value
        return self.result

    def divide(self, value):
        """Divides the current result by a number, handling division by zero."""
        if value == 0:
            raise ValueError("Cannot divide by zero")
        self.result /= value
        return self.result

    def clear(self):
        """Resets the result to zero."""
        self.result = 0
        return self.result

    def calculate(self, expression):
        """Evaluates a mathematical expression and updates the result."""
        try:
            self.result = eval(expression)
            return self.result
        except Exception as e:
            raise ValueError(f"Invalid expression: {e}")
