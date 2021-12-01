import unittest

from rectangle import area, peremiter


class TestArea(unittest.TestCase):
	def test_area(self):
		self.assertEqual(area(4, 5), 20)

	def test_area_incorrect_type_should_raise_error(self):
		self.assertRaises(TypeError, area, '4', 5)
		self.assertRaises(TypeError, area, 4, '5')

	def test_area_negative_value_should_raise_error(self):
		self.assertRaises(ValueError, area, -4, 5)
		self.assertRaises(ValueError, area, 4, -5)


class TestPeremiter(unittest.TestCase):
	def test_peremiter(self):
		self.assertEqual(peremiter(4, 5), 18)

	def test_peremiter_incorrect_type_should_raise_error(self):
		self.assertRaises(TypeError, peremiter, '4', 5)
		self.assertRaises(TypeError, peremiter, 4, '5')

	def test_peremiter_negative_value_should_raise_error(self):
		self.assertRaises(ValueError, peremiter, -4, 5)
		self.assertRaises(ValueError, peremiter, 4, -5)
