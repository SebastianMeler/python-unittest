import unittest

from tax import calc_tax


class TestCalcTax(unittest.TestCase):
	def test_calc_tax_with_incorrect_age_type_should_raise_type_error(self):
		self.assertRaises(TypeError, calc_tax, 100, 0.23, 'age')

	def test_calc_tax_with_negative_age_type_should_raise_error(self):
		self.assertRaises(ValueError, calc_tax, 100, 0.23, -1)

	def test_calc_tax_for_age_18_should_not_be_more_than_5000(self):
		self.assertLessEqual(calc_tax(1000000000, 0.23, 15), 5000)

	def test_calc_tax_for_age_30(self):
		self.assertEqual(calc_tax(10000, 0.23, 30), 2300)

	def test_calc_tax_for_age_70_should_not_be_more_than_8000(self):
		self.assertLessEqual(calc_tax(1000000000, 0.23, 70), 8000)
