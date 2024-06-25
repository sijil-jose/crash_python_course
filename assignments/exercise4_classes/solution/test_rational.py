import unittest
from Rational import Rational 
class TestRational(unittest.TestCase):
    def test_initialization(self):
        r = Rational(0.5)
        self.assertEqual(r.numerator, 1)
        self.assertEqual(r.denominator, 2)
        
        r = Rational(0.25)
        self.assertEqual(r.numerator, 1)
        self.assertEqual(r.denominator, 4)
        
        r = Rational(1.5)
        self.assertEqual(r.numerator, 3)
        self.assertEqual(r.denominator, 2)
        
        r = Rational(-0.5)
        self.assertEqual(r.numerator, -1)
        self.assertEqual(r.denominator, 2)

    def test_addition(self):
        r1 = Rational(1/2)
        r2 = Rational(1/3)
        r3 = r1 + r2
        self.assertEqual(r3.numerator, 5)
        self.assertEqual(r3.denominator, 6)

    def test_subtraction(self):
        r1 = Rational(1/2)
        r2 = Rational(1/3)
        r3 = r1 - r2
        self.assertEqual(r3.numerator, 1)
        self.assertEqual(r3.denominator, 6)

    def test_multiplication(self):
        r1 = Rational(1/2)
        r2 = Rational(1/3)
        r3 = r1 * r2
        self.assertEqual(r3.numerator, 1)
        self.assertEqual(r3.denominator, 6)

    def test_division(self):
        r1 = Rational(1/2)
        r2 = Rational(1/3)
        r3 = r1 / r2
        self.assertEqual(r3.numerator, 3)
        self.assertEqual(r3.denominator, 2)

    def test_equality(self):
        r1 = Rational(1/2)
        r2 = Rational(1/2)
        self.assertTrue(r1 == r2)

    def test_inequality(self):
        r1 = Rational(1/2)
        r2 = Rational(1/3)
        self.assertTrue(r1 != r2)

    def test_comparisons(self):
        r1 = Rational(1/2)
        r2 = Rational(1/3)
        self.assertTrue(r1 > r2)
        self.assertTrue(r2 < r1)
        self.assertTrue(r1 >= r2)
        self.assertTrue(r2 <= r1)

    def test_float_conversion(self):
        r = Rational(1/2)
        self.assertAlmostEqual(float(r), 0.5, places=5)

    def test_int_conversion(self):
        r = Rational(1.5)
        self.assertEqual(int(r), 1)

    def test_string_representation(self):
        r = Rational(1/2)
        self.assertEqual(str(r), "1/2")

    def test_repr(self):
        r = Rational(1/2)
        self.assertEqual(repr(r), "Rational(1, 2, precision=1e-05)")

    def test_invalid_precision(self):
        with self.assertRaises(ValueError):
            Rational(1/2, precision=-0.1)
        with self.assertRaises(ValueError):
            Rational(1/2, precision=1.1)

    def test_zero_denominator(self):
        with self.assertRaises(ZeroDivisionError):
            Rational(1, precision=1e-5, max_iterations=100)._float_to_rational(1/0)

if __name__ == "__main__":
    unittest.main()

