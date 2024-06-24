#File test_prime_factors.py

import unittest
from prime_factors import prime_factors


def multiplyList(List):
    '''
    returns product of all the elements of a list
    
    Paramteres
    ----------

    List : list
        the list whose prodcut of elements needs to be caluclated. where each element is an int

    Returns
    -------
    : int
        product of all the elements of the list

    '''

    # Multiply elements one by one
    result = 1
    for x in List:
        result = result * x
    return result


class TestPrimeFactors(unittest.TestCase):

    def test_prime_factors_product(self):
        for num in range(1, 101):
            with self.subTest(number=num):
                factors = prime_factors(num)
                product_of_factors = multiplyList(factors)
                self.assertEqual(product_of_factors, num, f"Failed for {num}")

if __name__ == "__main__":
    unittest.main()

