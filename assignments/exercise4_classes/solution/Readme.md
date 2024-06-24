A python package that enables rational number representation of integers and floats upt to given precision. The approximations are made using the [continued fraction](https://en.wikipedia.org/wiki/Continued_fraction) implemented in the ```_float_to_rational``` method.The ```_simplify``` method makes sure that there are no common factors between the numerator and denominator. _simply method is called in the initialisation of the class, thus making sure that the rational numbers are always simplified.
```max_iteration``` argument is used to restrict the numerators and denominators from blowing up to huge numbers. In such numbers the required precision might not be attained.

overload of __str__ and __repr__:,overload of the arithmetic dundler functions (e.g. __add__, __mul__, ...),
and overload of the comparison operators (e.g. __eq__, __gt__, ...) have been made.

The tests are in ```test_rational.py```. 
