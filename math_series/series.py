
# Check Edge Cases
if !(n == int):
    return ('Please enter a number!')


#Check Functionality
def fibonacci(n):
    if n < 0:
        print ('Please enter a number 0 or larger!')
        elif n < 2:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)


def lucas(n: int) -> int:
    if n < 0:
        print ('Please enter a number 0 or larger!')
        elif n = 0:
            return 2
        elif n = 1:
            return 1
        else:
            return lucas(n-1) + lucas(n-2)