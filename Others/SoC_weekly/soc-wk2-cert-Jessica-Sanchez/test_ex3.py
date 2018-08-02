#C:\Users\Public\Online_Courses\SOC\WK2\wk2_HW
#test_ex3.py

import unittest

# W2.D3.17	test to check the outcome of the alice_in_wonderfland, List of Lists

# W2.D3.18	test to check the outcome of the alice_in_wonderfland, Dict

from ex3 import *

class TestAlice(unittest.TestCase):

	def test0(self):
		self.assertEqual(freq_distribution('a'), ['a', 9804])

	def test1(self):
		self.assertEqual(freq_distribution2('a'), {'a': 9804})

	def test2(self):
		self.assertEqual(freq_distribution('j'), ['j', 235])

	def test3(self):
		self.assertEqual(freq_distribution2('j'), {'j': 235})

	def test4(self):
		self.assertEqual(freq_distribution('z'), ['z', 80])

	def test5(self):
		self.assertEqual(freq_distribution2('z'), {'z': 80})

unittest.main()