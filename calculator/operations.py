import math

def add(x, y):
    result = x + y
    if math.isinf(result):
        return None
    return result

def subtract(x, y):
    result = x - y
    if math.isinf(result):
        return None
    return result

def multiply(x, y):
    result = x * y
    if math.isinf(result):
        return None
    return result

def divide(x, y):
    if y == 0:
        return None

    result = x / y

    if math.isinf(result):
        return None

    return result

def factorial(n):

    if n < 0 or n > 170:
        return None

    fact = 1.0

    for i in range(1, n + 1):
        fact *= i

        if math.isinf(fact):
            return None

    return fact

def ln(x):

    if x <= 0:
        return None

    return math.log(x)

def power(x, y):

    if x == 0 and y == 0:
        return None

    result = math.pow(x, y)

    if math.isinf(result):
        return None

    return result

def sqrt(x):

    if x < 0:
        return None

    return math.sqrt(x)