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
        real : float
            the real component of the imaginary number (default value = 0.0)
        imaginary : float
            the imaginary component of the imaginary number (default value = 0.0)
        """
        self.real = real
        self.imaginary = imaginary

    def add(self, to_add: object):
        """
        Adds two imaginary numbers, one being the one that this method is applied to, and the other one being to_add,
        both being ImaginaryNumbers objects.

        Parameters
        ----------
        to_add : object
            An ImaginaryNumber object that needs to be added to the initial ImaginaryNumber object.

        Returns
        -------
        ImaginaryNumber object:
            A new ImaginaryNumber object that will contain the sum between the real part of the applied object
            with the real part of the to_add object, respectively the sum between the imaginary part of the
            object that has this method applied and to_add imaginary part.
        """
        if type(to_add) == ImaginaryNumber:
            return ImaginaryNumber(self.real + to_add.real, self.imaginary + to_add.imaginary)
        else:
            raise AttributeError(f"Wrong type of object passed to the addition method.")

    def substraction(self, to_substract: object):
        """
        Substracts two imaginary numbers, one being the one that this method is applied to, and the other one being
        to_substract, both being ImaginaryNumbers objects.

        Parameters
        ----------
        to_substract : object
            An ImaginaryNumber object that needs to be substracted from the initial ImaginaryNumber object.

        Returns
        -------
        ImaginaryNumber object:
            A new ImaginaryNumber object that will contain the difference between the real part of the applied object
            with the real part of the to_substract object, respectively the difference between the imaginary part of
            the object that has this method applied and to_substract imaginary part.
        """
        if type(to_substract) == ImaginaryNumber:
            return ImaginaryNumber(self.real + to_substract.real, self.imaginary + to_substract.imaginary)
        else:
            raise AttributeError(f"Wrong type of object passed to the substraction method.")

    def __str__(self):
        if self.im == 0:
            return f'{self.real:2f}'
        if self.re == 0:
            return f'{self.imaginary:2f}i'
        if self.im < 0:
            return f"{self.real:2f} {'-' if self.imaginary < 0 else '+'} {self.imaginary:2f}i"
