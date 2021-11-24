import unittest


class TestCase(unittest.TestCase):

	def test_case_1(self):
		self.assertGreater(4, 3)

	def test_case_2(self):
		self.assertGreaterEqual(4, 4)

	def test_case_3(self):
		self.assertLess(2, 3)

	def test_case_4(self):
		self.assertLessEqual(3, 3)
