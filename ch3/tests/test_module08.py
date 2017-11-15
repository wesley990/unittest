import unittest
from features import test_me

'''
python -m unittest tests.test_module08 -v
'''

class TestClass09(unittest.TestCase):
  def test_case01(self):
    self.assertEqual(test_me.add(2, 3), 5)
    print("\nIn test_case01()")
  def test_case02(self):
    self.assertEqual(test_me.mul(2, 3), 6)
    print("\nIn test_case02()")