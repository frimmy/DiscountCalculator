import unittest
from discountCalcApp import DiscountCalculator

class DiscountCalculatorTests(unittest.TestCase):
	"""test suite for discount calculator"""
	def setUp(self):
		self.discount_calculator = DiscountCalculator()

	def test_ten_percent(self):
		
		result = self.discount_calculator.determine_discount(100, 10, 'percent')
		self.assertEqual(10.0, result)
		

	def fifteen_percent_discount_test(self):
		result = self.discount_calculator.determine_discount(100, 15, 'percent')
		self.assertEqual(15.0, result)

	def five_dollar_discount_test(self):
		result = self.discount_calculator.determine_discount(250, 5, 'value')
		self.assertEqual(5.0, result)

	def invalid_discount_type_test(self):

		self.assertRaises(ValueError, self.discount_calculator.determine_discount, 250, 5, 'random')

	def floating_point_percentage_discount_test(self):
		result = self.discount_calculator.determine_discount(100.0, 10.0, 'percent')
		self.assertEqual(10.0, result)

	def floating_point_value_discount_test(self):
		result = self.discount_calculator.determine_discount(250.0, 5.0, 'value')
		self.assertEqual(5.0, result)

