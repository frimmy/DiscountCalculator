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
		result = self.discount_calculator.determine_discount(100,15, 'percent')
		self.assertEqual(15.0, result)