import unittest
from test295assertraises import tourguide
class SomeTests(unittest.TestCase):
    def testing_for_error(self):
        """testing for an error"""
        placetogo = ['bali', 'sweden', 'egypt', 'fiji', 'san franciso']
        with self.assertRaises(IndexError):
            # tourguide("James", 100, placetogo) #ran OK
            tourguide("James", 1, placetogo) #AssertionError: IndexError not raised
if __name__ == "__main__":
    unittest.main()