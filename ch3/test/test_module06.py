import unittest

class TestClass07(unittest.TestCase):
    '''
    python -m unittest test_module06.py
    
    to run unit test without unittest.main()

    '''
    def test_case01(self):
            self.assertTrue("PYTHON".isupper())
            print("\nIn test_case01()")