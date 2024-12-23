def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def floor_divide(a, b):
    """Floor division of a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a // b

def modulus(a, b):
    """Return remainder of a divided by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a % b

def power(a, b):
    """Return a raised to power b"""
    return a ** b

def square_root(a):
    """Return square root of a"""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return a ** 0.5
