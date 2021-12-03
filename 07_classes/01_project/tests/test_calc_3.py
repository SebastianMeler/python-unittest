import unittest

from calculator.calc_mat import SimpleMatCalculator


class TestSimpleMatCalculatorAdd(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print('setting up class...')
		cls.calc = SimpleMatCalculator()

	@classmethod
	def tearDownClass(cls):
		print('tearing down class...')
		del cls.calc

	def test_add_int(self):
		self.assertEqual(self.calc.add(3, 4), 7)

	def test_add_float(self):
		self.assertEqual(self.calc.add(3.0, 4.0), 7.0)

	def test_add_negative(self):
		self.assertEqual(self.calc.add(-3, -4), -7)


class TestSimpleMatCalculatorSub(unittest.TestCase):

	def test_sub_int(self):
		calc = SimpleMatCalculator()
		self.assertEqual(calc.sub(3, 4), -1)

	def test_sub_float(self):
		calc = SimpleMatCalculator()
		self.assertEqual(calc.sub(3.0, 4.0), -1.0)
