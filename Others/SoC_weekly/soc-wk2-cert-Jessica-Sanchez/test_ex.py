#C:\Users\Public\Online_Courses\SOC\WK2\wk2_HW
#test_ex.py

# #Optional
# 	# If you have already started Python the Hard Way, please choose 5 exercises and write tests for those in unittest and 
# 	#make them pass. Take your ex.py and your test_ex.py and zip them into a single file to upload for submission via the Helpdesk.



import unittest

from ex import *

class TestConvert_to_roman2(unittest.TestCase):

	def test0(self):
		self.assertEqual(convert_to_roman(444), 'CCCCXXXXIIII')

	def test1(self):
		self.assertEqual(convert_to_roman2(400), 'CDXLIV')

	def test2(self):
		self.assertEqual(convert_to_roman(999), 'DCCCCLXXXXVIIII')

	def test3(self):
		self.assertEqual(convert_to_roman2(999), 'CMXCIX')

	def test4(self):
		self.assertEqual(convert_to_roman(1296), 'MCCLXXXXVI')

	def test5(self):
		self.assertEqual(convert_to_roman2(1296), 'MCCXCVI')


unittest.main()