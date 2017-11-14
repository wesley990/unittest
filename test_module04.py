import unittest
import inspect

'''
You can run the entire test module with the following command:
python3 -m unittest -v test_module04

You can run a single test class with the following command:
python3 -m unittest -v test_module04.TestClass04


'''

class TestClass04(unittest.TestCase):
        def test_case01(self):
                print("\nClassname : " + self.__class__.__name__)
                print("Running Test Method : " + inspect.stack()[0][3])
class TestClass05(unittest.TestCase):
        def test_case01(self):
                print("\nClassname : " + self.__class__.__name__)
                print("Running Test Method : " + inspect.stack()[0][3])
if __name__ == '__main__':
        unittest.main(verbosity=2)