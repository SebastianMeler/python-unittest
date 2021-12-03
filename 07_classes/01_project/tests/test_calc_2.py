import unittest

from calculator.calc_mat import SimpleMatCalculator


def setUpModule():
	print('setting up ...')
	global calc
	calc = SimpleMatCalculator()


def tearDownModule():
	print('tearing down ...')
	global calc
	del calc


class TestSimpleMatCalculator(unittest.TestCase):

	def test_add(self):
		self.assertEqual(calc.add(3, 4), 7)

	def test_sub(self):
		self.assertEqual(calc.sub(3, 4), -1)

	def test_mul(self):
		self.assertEqual(calc.mul(3, 4), 12)
