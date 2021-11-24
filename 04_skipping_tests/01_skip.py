import unittest


class TestClass(unittest.TestCase):

	def test_case_1(self):
		self.assertEqual("aws".upper(), "AWS")

	@unittest.skip("Always skiping...")
	def test_case_2(self):
		self.assertEqual("aws".upper(), "AWS")
