from math_series import __version__ 

from math_series.series import fibonacci, lucas 



def test_version():
    assert __version__ == '0.1.0'

def test_fib_one():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fib_two():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected    
    
def test_lucas_one():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_two():
    actual = lucas(1)
    expected = 1
    assert actual == expected

# def test_sum():
#     actual = fizz_buzz(5)
#     expected = 'Buzz'
#     assert actual == expected
