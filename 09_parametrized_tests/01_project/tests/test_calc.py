import unittest

from calculator.calc_mat import SimpleMatCalculator


class TestSimpleMatCalculator(unittest.TestCase):
	def setUp(self) -> None:
		self.calc = SimpleMatCalculator()

	def test_add(self):
		cases = [
			(-3, -2, -5),
			(-3, 2, -1),
			(3, -2, 1),
			(3, 2, 5)
		]
		for x, y, result in cases:
			with self.subTest(cases=cases):
				self.assertEqual(self.calc.add(x, y), result)
