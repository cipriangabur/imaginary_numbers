import unittest

from imaginary_numbers import ImaginaryNumber


class ImaginaryNumberTests(unittest.TestCase):

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
        data1 = [(1, 1), (1, -1), (-2, 2), (1.5, 3.2), (2, 2)]
        data2 = [(2, 1), (2, 1), (4, 4), (1.2, -2.2), (0, 0)]
        expected = ["3 + 2i", "3 + 0i", "2 + 6i", "2.7 + 1i", "2 + 2i"]
        for index, _ in  enumerate(data1):
            obj1 = ImaginaryNumber(*data1[index])
            obj2 = ImaginaryNumber(*data2[index])
            self.assertEqual(expected[index], obj1.add(obj2).__str__())

    def test_addition_negative_test(self):
        obj1 = ImaginaryNumber()
        obj2 = "string object"
        with self.assertRaises(AttributeError):
            obj1.add(obj2)
