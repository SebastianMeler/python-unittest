import unittest

from calculator.calc_mat import SimpleMatCalculator
from parameterized import parameterized


class TestSimpleMatCalculator(unittest.TestCase):
	def setUp(self) -> None:
		self.calc = SimpleMatCalculator()

	@parameterized.expand([
		('negative', -3, -2, -5),
		('mixed', -3, 2, -1),
		('mixed', 3, -2, 1),
		('positive', 3, 2, 5)
	])
	def test_add(self, name, x, y, result):
		self.assertEqual(self.calc.add(x, y), result)
