import unittest

import Jumpernu

class TestJumper(unittest.TestCase):
	def test_one(self):
		solutionFound = Jumpernu.solve_equation_for_range(0, 10, 1)

		self.assertTrue(solutionFound)

if __name__ == '__main__':
    unittest.main()

