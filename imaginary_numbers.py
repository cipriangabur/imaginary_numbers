class ImaginaryNumber:
    """
    A class used to represent an Imaginary Number.

    ...
    Attributes
    ----------
    real : float
        the real component of the imaginary number
    imaginary : float
        the imaginary component of the imaginary number

    Methods
    -------
    method(param=value)
        description
    """

    def __init__(self, real=0.0, imaginary=0.0):
        """
        Class constructor

        Parameters
        ----------
        self : object
            An instance of the ImaginaryNumbers class
        real : float
            the real component of the imaginary number (default value = 0.0)
        imaginary : float
            the imaginary component of the imaginary number (default value = 0.0)
        """

        def filter_values_type(x):
            return x if isinstance(x, (int, float)) and not isinstance(x, bool) else 0

        self.real = filter_values_type(real)
        self.imaginary = filter_values_type(imaginary)

    def __add__(self, other):
        """
        Adds two imaginary numbers, one being the one that this method is applied to, and the other object,
        both being ImaginaryNumbers objects.

        Parameters
        ----------
        self : object
            An instance of the ImaginaryNumbers class
        other : object
            An ImaginaryNumber object that needs to be added to the initial ImaginaryNumber object.

        Returns
        -------
        ImaginaryNumber object:
            A new ImaginaryNumber object that will contain the sum between the real part of the applied object
            with the real part of the other object, respectively the sum between the imaginary part of the
            object that has this method applied and other imaginary part.
        """
        if type(other) == ImaginaryNumber:
            return ImaginaryNumber(self.real + other.real, self.imaginary + other.imaginary)
        else:
            raise AttributeError(f"Wrong type of object passed to the addition method.")

    def __sub__(self, to_subtract: object):
        """
        Subtracts two imaginary numbers, one being the one that this method is applied to, and the other one being
        to_subtract, both being ImaginaryNumbers objects.

        Parameters
        ----------
        self : object
            An instance of the ImaginaryNumbers class
        to_subtract : object
            An ImaginaryNumber object that needs to be subtracted from the initial ImaginaryNumber object.

        Returns
        -------
        ImaginaryNumber object:
            A new ImaginaryNumber object that will contain the difference between the real part of the applied object
            with the real part of the to_subtract object, respectively the difference between the imaginary part of
            the object that has this method applied and to_subtract imaginary part.
        """
        if type(to_subtract) == ImaginaryNumber:
            return ImaginaryNumber(self.real - to_subtract.real, self.imaginary - to_subtract.imaginary)
        else:
            raise AttributeError(f"Wrong type of object passed to the subtraction method.")

    def __mul__(self, to_multiply: object):
        """
        Multiply two imaginary numbers, one being the one that this method is applied to, and the other one being
        to_multiply, both being ImaginaryNumbers objects.

        Parameters
        ----------
        self : object
            An instance of the ImaginaryNumbers class
        to_multiply : object
            An ImaginaryNumber object that needs to be multiplied with the initial ImaginaryNumber object.

        Returns
        -------
        ImaginaryNumber object:
            A new ImaginaryNumber object that will contain the multiplication between the object that this method is
            applied to, and to_multiply ImaginaryNumber object. The simplified equation would reduce to :
            (a+bi)(c+di) = (ac−bd)+(ad+bc)i.
        """
        if type(to_multiply) == ImaginaryNumber:
            a, b = self.real, self.imaginary
            c, d = to_multiply.real, to_multiply.imaginary
            return ImaginaryNumber(a * c - b * d, b * c + a * d)
        else:
            raise AttributeError(f"Wrong type of object passed to the multiplication method.")

    def __truediv__(self, to_divide: object):
        """
        Divide two imaginary numbers, one being the one that this method is applied to, and the other one being
        to_divide, both being ImaginaryNumbers objects.

        Parameters
        ----------
        self : object
            An instance of the ImaginaryNumbers class
        to_divide : object
            An ImaginaryNumber object that needs to be divided with the initial ImaginaryNumber object.

        Returns
        -------
        ImaginaryNumber object:
            A new ImaginaryNumber object that will contain the division between the object that this method is
            applied to, and to_divide ImaginaryNumber object. The simplified equation would reduce to :
            (a + bi) / (c + di) = ((ac + bd) + (bc - ad) i) / c * c + d * d
        """

        if type(to_divide) == ImaginaryNumber:
            a, b = self.real, self.imaginary
            c, d = to_divide.real, to_divide.imaginary
            denominator = c ** 2 + d ** 2
            return ImaginaryNumber((a * c + b * d) / denominator, (b * c - a * d) / denominator)
        else:
            raise AttributeError(f"Wrong type of object passed to the division method.")

    def completely_imaginary(self):
        """
        Method designed to return True if a certain object is representing a pure imaginary number or False
        otherwise

        Parameters
        ----------
        self : object
            An instance of the ImaginaryNumbers class

        Returns
        -------
        bool:
            True if the ImaginaryNumber has the real component equal to zero, False otherwise.
        """
        return self.real == 0

    def completely_real(self):
        """
        Method designed to return True if a certain object is representing a pure real number or False
        otherwise.

        Parameters
        ----------
        self : object
            An instance of the ImaginaryNumbers class

        Returns
        -------
        bool:
            True if the ImaginaryNumber has the imaginary component equal to zero, False otherwise.
        """
        return self.imaginary == 0

    def __str__(self):
        """
        Method designed to return a certain string when called or when the ImaginaryNumber object is printed.

        Parameters
        ----------
        self : object
            An instance of the ImaginaryNumbers class

        Returns
        -------
        formatted string: str
            A formatted string representing the imaginary number (e.g. 1 + 2i)
        """

        return f"{self.real:g} {'-' if self.imaginary < 0 else '+'} {abs(self.imaginary):g}i"

    # TODO: A method that has the purpose of calculating the modulus of an imaginary number
    #  (sqrt(real**2 + imaginary**2) )

    # TODO: A method used to check the equality between two ImaginaryNumbers objects

    # TODO: A method to return the conjugate of a specific ImaginaryNumber object
    #  (for z = a + bj, the conjugate would be z1 = a - bj)

    # TODO: Method to calculate the square root of a specific ImaginaryNumber object

    # TODO: A method to plot a specific complex number in a 2D axes system
