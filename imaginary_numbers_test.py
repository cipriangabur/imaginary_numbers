import unittest

from imaginary_numbers import ImaginaryNumber


class ImaginaryNumberTests(unittest.TestCase):

    data1 = [(1, 1), (1, -1), (-2, 2), (1.5, 3.2), (2, 2)]
    data2 = [(2, 1), (2, 1), (4, 4), (1.2, -2.2), (0, 0)]

    add_expected = ["3 + 2i", "3 + 0i", "2 + 6i", "2.7 + 1i", "2 + 2i"]
    sub_expected = ["-1 + 0i", "-1 - 2i", "-6 - 2i", "0.3 + 5.4i", "2 + 2i"]
    mul_expected = ["1 + 3i", "3 - 1i", "-16 + 0i", '8.84 + 0.54i', "0 + 0i"]
    div_expected = ["0.6 + 0.2i", "0.2 - 0.6i", "0 + 0.5i", '-0.834395 + 1.13694i']

    def test_object_creation_valid_data_ints(self):
        self.assertEqual("1 + 2i", str(ImaginaryNumber(1, 2)))

    def test_object_creation_valid_data_floats(self):
        self.assertEqual("1.5 + 2.2i", str(ImaginaryNumber(1.5, 2.2)))

    def test_object_creation_empty_data(self):
        self.assertEqual("0 + 0i", str(ImaginaryNumber()))

    def test_object_creation_wrong_data_string_both(self):
        self.assertEqual('0 + 0i', str(ImaginaryNumber('a', 'b')))

    def test_object_creation_wrong_data_string_real(self):
        self.assertEqual('0 + 1i', str(ImaginaryNumber('a', 1)), '0 + 1i')

    def test_object_creation_wrong_data_string_imaginary(self):
        self.assertEqual('1 + 0i', str(ImaginaryNumber(1, '1')))

    def test_object_creation_wrong_data_bool_imaginary(self):
        obj = ImaginaryNumber(real=1, imaginary=False)
        self.assertEqual('1 + 0i', str(obj))

    def test_object_creation_wrong_data_bool_real(self):
        obj = ImaginaryNumber(real=True, imaginary=1)
        self.assertEqual('0 + 1i', str(obj))

    def test_object_pure_imaginary(self):
        obj = ImaginaryNumber()
        self.assertEqual(True, obj.completely_imaginary())

    def test_object_pure_imaginary_negative(self):
        obj = ImaginaryNumber(real=5, imaginary=4)
        self.assertEqual(False, obj.completely_imaginary())

    def test_object_pure_real(self):
        obj = ImaginaryNumber()
        self.assertEqual(True, obj.completely_real())

    def test_object_pure_real_negative(self):
        obj = ImaginaryNumber(imaginary=2)
        self.assertEqual(False, obj.completely_real())

    def test_printing_of_object_data(self):
        obj = ImaginaryNumber(imaginary=2, real=3)
        self.assertEqual(obj.__str__(), str(obj))

    def test_addition_happy_flow(self):
        for index, _ in enumerate(self.data1):
            obj1 = ImaginaryNumber(*self.data1[index])
            obj2 = ImaginaryNumber(*self.data2[index])
            self.assertEqual(self.add_expected[index], str(obj1 + obj2))

    def test_substraction_happy_flow(self):
        for index, _ in enumerate(self.data1):
            obj1 = ImaginaryNumber(*self.data1[index])
            obj2 = ImaginaryNumber(*self.data2[index])
            self.assertEqual(self.sub_expected[index], str(obj1 - obj2))

    def test_multiplication_happy_flow(self):
        for index, _ in enumerate(self.data1):
            obj1 = ImaginaryNumber(*self.data1[index])
            obj2 = ImaginaryNumber(*self.data2[index])
            self.assertEqual(self.mul_expected[index], str(obj1 * obj2))

    def test_division_happy_flow(self):
        for index, _ in enumerate(self.data1[:-1]):  # Otherwise will trigger ZeroDivisionError exception
            obj1 = ImaginaryNumber(*self.data1[index])
            obj2 = ImaginaryNumber(*self.data2[index])
            self.assertEqual(self.div_expected[index], str(obj1 / obj2))

    def test_addition_negative_test_1(self):
        obj1 = ImaginaryNumber()
        obj2 = "string object"
        with self.assertRaises(AttributeError):
            obj1.__add__(obj2)

    def test_addition_negative_test_2(self):
        obj1 = None
        obj2 = "string object"
        with self.assertRaises(AttributeError):
            obj1.__add__(obj2)

    def test_addition_negative_test_3(self):
        obj1 = None
        obj2 = ImaginaryNumber()
        with self.assertRaises(AttributeError):
            obj1.__add__(obj2)

    # TODO: substraction negative tests

    # TODO: multiplication negative tests for AttributeError

    # TODO: Add addition/multiplication happy flows for testing addition/multiplication properties
    #  (associativity, commutativity, etc).

    # TODO: add division negative tests for AttributeError

    # TODO: Add division negative tests for ZeroDivisionError
