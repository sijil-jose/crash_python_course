#File: ex3.2_solution.py

def fibonacci (n):
    """A function that calculates the Fibonacci sequence up to the n-th term

    Parameters
    ----------
    n : int 
        the n-th term of the sequence

    Returns
    -------
    : list
        
        a list with the Fibonacci sequence if n >= 3
        returns [0] if n = 1
        returns [0, 1] if n = 2
        returns [] if n <= 0 or other wise 

    """
    if isinstance(n, int) == False:
      return []
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    
    return fib_sequence


# writing unit tests for the function fibonacci() :

import unittest

class TestFibonacciFunction(unittest.TestCase):

    def test_fibonacci_zero(self):
        self.assertEqual(fibonacci(0), [])

    def test_fibonacci_one(self):
        self.assertEqual(fibonacci(1), [0])

    def test_fibonacci_two(self):
        self.assertEqual(fibonacci(2), [0, 1])

    def test_fibonacci_ten(self):
        self.assertEqual(fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_fibonacci_negative(self):
        self.assertEqual(fibonacci(-5), [])

    def test_fibonacci_nonint(self):
        self.assertEqual(fibonacci(5.6), [])


if __name__ == '__main__' :
   unittest.main()

