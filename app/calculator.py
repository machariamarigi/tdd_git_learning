"""This module contains the calculator logic application encapsulted in the
    Calculator class
"""


class Calculator(object):
    """This class contains methods that accomplish arithmetic maipulation of
        numbers
    """

    def add(self, val1, val2):
        """Method that performs the adding arithmetic operation of 2 numbers
            passed in the th argument
        """

        number_types = (int, float, complex)

        if isinstance(val1, number_types) and isinstance(val2, number_types):
            return val1 + val2
        else:
            raise ValueError
