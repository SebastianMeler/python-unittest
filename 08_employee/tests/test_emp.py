import unittest

from employee.emp import Employee


class TestEmployee(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		print('setting up class...')
		cls.emp = Employee("Sebastian", "Meler", "100000")
		cls.emp.tax_rate = 0.17
		cls.emp.bonus_rate = 0.10

	def test_email_created(self):
		self.assertEqual(self.emp.email, "sebastian.meler@mail.com")

	def test_correct_tax_rate(self):
		self.assertEqual(self.emp.tax, 17000)

	def test_correct_apply_bonus(self):
		self.assertEqual(self.emp.apply_bonus(), 110000)
