#File prime_factors.py

def prime_factors(n):
    """
    Returns the prime factorization of a given positive integer n.
    
    Parameters
    ----------
    n : int
        the number whose prime factors needs to be found out

    Returns
    -------
    : list

        a list with all the prime factors
        returns [] if n <= 1

    """
    if n <= 1:
        return []
    factors = []
    # Check for number of 2s in n
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Check for odd factors from 3 onwards
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    # If n is still a prime number greater than 2
    if n > 2:
        factors.append(n)
    return factors
