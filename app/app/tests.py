# Python tests
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        res = calc.add(5, 6)

        self.assertAlmostEqual(res, 11)

    def test_subtract_numbers(self):
        # subtracts numbers
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)
