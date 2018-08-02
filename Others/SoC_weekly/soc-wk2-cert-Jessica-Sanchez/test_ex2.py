#test_ex2.py
import unittest

from ex2 import *

print('\nW2.D2.12 Continent Counter Test\n\n') 

# W2.D2.12	Continent Counter Test
	# Write test coverage in unittest and/or trace for Continent Counter. (I did it for my Continer Counter)


class TestContinentCounter(unittest.TestCase):


	def test0(self):
		self.assertEqual(continent_counter(1,1),26)

	def test1(self):
		self.assertEqual(continent_counter(6,10),20)


	def test2(self):
		self.assertEqual(continent_counter(2,9),2)

unittest.main()