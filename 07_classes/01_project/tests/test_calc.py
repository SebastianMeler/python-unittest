import unittest

from calculator.calc_mat import SimpleMatCalculator


class TestSimpleMatCalculator(unittest.TestCase):
	def test_add(self):
		calc = SimpleMatCalculator()
		self.assertEqual(calc.add(3, 4), 7)

	def test_sub(self):
		calc = SimpleMatCalculator()
		self.assertEqual(calc.sub(3, 4), -1)

	def test_mul(self):
		calc = SimpleMatCalculator()
		self.assertEqual(calc.mul(3, 4), 12)
