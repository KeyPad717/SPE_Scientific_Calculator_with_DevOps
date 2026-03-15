from calculator.operations import *

def test_add():
    assert add(2,3) == 5

def test_subtract():
    assert subtract(10,4) == 6

def test_multiply():
    assert multiply(3,4) == 12

def test_divide():
    assert divide(10,2) == 5

def test_divide_zero():
    assert divide(5,0) == None
#test
def test_factorial():
    assert factorial(5) == 120

def test_ln():
    assert round(ln(1),5) == 0
#ttr
def test_power():
    assert power(2,3) == 8

def test_sqrt():
    assert sqrt(16) == 4