import unittest
from add import adds 

class test_add_sol(unittest.TestCase):
	def test_add(self):
		result = self.adds(2,2)
		self.assertEqual(result,4)