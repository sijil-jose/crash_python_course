#File: ex3.4_solution.py

def sieve_of_sundaram(max_n):
    '''
    A function that calculates list of prime numbers below a max n using sieve of sundaram algorithm O(nlogn):

    Parameters
    ----------
    max_n : int
           upper limit

    Returns
    -------
    : list

        a list with prime numbers below n_max
        returns [] if n < 2
    '''
    # Calculate the integer limit for the sieve
    n = (max_n - 1) // 2
    # Initialize a list of True values
    sieve = [True] * (n + 1)

    # Use the Sieve of Sundaram to eliminate indices
    for i in range(1, n + 1):
        j = i
        while (i + j + 2 * i * j) <= n:
            sieve[i + j + 2 * i * j] = False
            j += 1

    # Generate the list of primes less than max_n
    primes = [2] if max_n > 2 else []
    primes.extend([2 * i + 1 for i in range(1, n + 1) if sieve[i]])

    return primes

# Generate and print primes below 100
primes_below_100 = sieve_of_sundaram(100)
print(primes_below_100)


# writing unittests for the function

import unittest

class TestSieveOfSundaram(unittest.TestCase):
    def test_primes_below_10(self):
        self.assertEqual(sieve_of_sundaram(10), [2, 3, 5, 7])

    def test_primes_below_30(self):
        self.assertEqual(sieve_of_sundaram(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    def test_primes_below_2(self):
        self.assertEqual(sieve_of_sundaram(2), [])

    def test_primes_below_1(self):
        self.assertEqual(sieve_of_sundaram(1), [])

if __name__ == '__main__':
    unittest.main()

