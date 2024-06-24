from math import gcd

class Rational:
    def __init__(self, number, *, precision=1e-5, max_iterations=100):
        """
        Initializes a Rational object from a floating-point number.

        Parameters:
        number (float): The floating-point number to be converted to a rational number.
        precision (float): The precision for the conversion. Must be between 0 and 1.
        max_iterations (int): The maximum number of iterations to find the rational approximation.

        Raises:
        ValueError: If precision is not between 0 and 1.
        """
        if precision <= 0 or precision >= 1:
            raise ValueError("Precision must be between 0 and 1.")
        
        self.precision = precision
        self.max_iterations = max_iterations
        self.numerator, self.denominator = self._float_to_rational(number)
        self._simplify()

    def _float_to_rational(self, number):
        """
        Converts a floating-point number to a rational number.

        Parameters:
        number (float): The floating-point number to be converted.

        Returns:
        tuple: A tuple containing the numerator and denominator of the rational number.
        """
        if number < 0:
          sign = -1
        else :
          sign = 1
        number = abs(number)
        # working only with positive numbers and adding the sign back at the end.

        def fraction_from_continued(cont):
            num = 1
            denom = cont.pop()
            while cont:
                num, denom = denom, denom * cont.pop() + num
            return denom, num

        def get_continued_fraction(num, precision, max_iterations):
            cont = []
            iterations = 0
            while abs(num - round(num)) > precision and iterations < max_iterations:
                integral_part = int(num)
                cont.append(integral_part)
                num = 1 / (num - integral_part)
                iterations += 1
            cont.append(int(num + 0.5))
            return cont

        cont_frac = get_continued_fraction(number, self.precision, self.max_iterations)
        numerator, denominator = fraction_from_continued(cont_frac)

        if sign == -1:
          numerator = sign*numerator
        return numerator, denominator

    def _simplify(self):
        """
        Simplifies the rational number by dividing the numerator and denominator
        by their greatest common divisor.

        decided to use the gcd function from math instead of the function defined in the previous exercise
        """
        common_factor = gcd(self.numerator, self.denominator)
        self.numerator //= common_factor
        self.denominator //= common_factor
        if self.denominator < 0:  # Ensuring the denominator is always positive
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __abs__(self):
        """
        Returns the absolute value of the rational number.

        Returns:
        Rational: The absolute value of the rational number.
        """
        return Rational(abs(self.numerator) / self.denominator, precision=self.precision, max_iterations=self.max_iterations)

    def __str__(self):
        """
        Returns the string representation of the rational number.

        Returns:
        str: The string representation of the rational number in the form 'numerator/denominator'.
        """
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        """
        Returns the official string representation of the rational number.

        Returns:
        str: The official string representation of the rational number.
        """
        return f"Rational({self.numerator}, {self.denominator}, precision={self.precision})"

    def __add__(self, other):
        """
        Adds another rational number or a floating-point number to the current rational number.

        Parameters:
        other (Rational, int, float): The number to be added.

        Returns:
        Rational: The sum of the two numbers.
        """
        if isinstance(other, Rational):
            num = self.numerator * other.denominator + other.numerator * self.denominator
            den = self.denominator * other.denominator
        elif isinstance(other, (int, float)):
            other_rational = Rational(other, precision=self.precision, max_iterations=self.max_iterations)
            return self + other_rational
        else:
            return NotImplemented
        return Rational(num / den, precision=self.precision, max_iterations=self.max_iterations)

    def __sub__(self, other):
        """
        Subtracts another rational number or a floating-point number from the current rational number.

        Parameters:
        other (Rational, int, float): The number to be subtracted.

        Returns:
        Rational: The difference between the two numbers.
        """
        if isinstance(other, Rational):
            num = self.numerator * other.denominator - other.numerator * self.denominator
            den = self.denominator * other.denominator
        elif isinstance(other, (int, float)):
            other_rational = Rational(other, precision=self.precision, max_iterations=self.max_iterations)
            return self - other_rational
        else:
            return NotImplemented
        return Rational(num / den, precision=self.precision)

    def __mul__(self, other):
        """
        Multiplies the current rational number by another rational number or a floating-point number.

        Parameters:
        other (Rational, int, float): The number to multiply by.

        Returns:
        Rational: The product of the two numbers.
        """
        if isinstance(other, Rational):
            num = self.numerator * other.numerator
            den = self.denominator * other.denominator
        elif isinstance(other, (int, float)):
            other_rational = Rational(other, precision=self.precision, max_iterations=self.max_iterations)
            return self * other_rational
        else:
            return NotImplemented
        return Rational(num / den, precision=self.precision)

    def __truediv__(self, other):
        """
        Divides the current rational number by another rational number or a floating-point number.

        Parameters:
        other (Rational, int, float): The number to divide by.

        Returns:
        Rational: The quotient of the division.
        """
        if isinstance(other, Rational):
            num = self.numerator * other.denominator
            den = self.denominator * other.numerator
        elif isinstance(other, (int, float)):
            other_rational = Rational(other, precision=self.precision, max_iterations=self.max_iterations)
            return self / other_rational
        else:
            return NotImplemented
        return Rational(num / den, precision=self.precision)

    def __eq__(self, other):
        """
        Checks if the current rational number is equal to another rational number or a floating-point number.

        Parameters:
        other (Rational, int, float): The number to compare with.

        Returns:
        bool: True if the numbers are equal, False otherwise.
        """
        if isinstance(other, Rational):
            return self.numerator * other.denominator == self.denominator * other.numerator
        elif isinstance(other, (int, float)):
            return float(self) == other
        else:
            return NotImplemented

    def __lt__(self, other):
        """
        Checks if the current rational number is less than another rational number or a floating-point number.

        Parameters:
        other (Rational, int, float): The number to compare with.

        Returns:
        bool: True if the current number is less than the other number, False otherwise.
        """
        if isinstance(other, Rational):
            return self.numerator * other.denominator < self.denominator * other.numerator
        elif isinstance(other, (int, float)):
            return float(self) < other
        else:
            return NotImplemented

    def __le__(self, other):
        """
        Checks if the current rational number is less than or equal to another rational number or a floating-point number.

        Parameters:
        other (Rational, int, float): The number to compare with.

        Returns:
        bool: True if the current number is less than or equal to the other number, False otherwise.
        """
        return self < other or self == other

    def __gt__(self, other):
        """
        Checks if the current rational number is greater than another rational number or a floating-point number.

        Parameters:
        other (Rational, int, float): The number to compare with.

        Returns:
        bool: True if the current number is greater than the other number, False otherwise.
        """
        return not self <= other

    def __ge__(self, other):
        """
        Checks if the current rational number is greater than or equal to another rational number or a floating-point number.

        Parameters:
        other (Rational, int, float): The number to compare with.

        Returns:
        bool: True if the current number is greater than or equal to the other number, False otherwise.
        """
        return not self < other

    def __int__(self):
        """
        Returns the integer representation of the rational number.

        Returns:
        int: The integer representation of the rational number.
        """
        return self.numerator // self.denominator

    def __float__(self):
        """
        Returns the floating-point representation of the rational number.

        Returns:
        float: The floating-point representation of the rational number.
        """
        return self.numerator / self.denominator

