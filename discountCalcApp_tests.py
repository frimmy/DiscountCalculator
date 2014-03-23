import unittest
from discountCalcApp import DiscountCalculator

class DiscountCalculatorTests(unittest.TestCase):
	"""test suite for discount calculator"""
	def test_ten_percent(self):
		discount_calculator = DiscountCalculator()
		result = discount_calculator.determine_discount(100, 10, 'percent')
		self.assertEqual(10.0, result)
		