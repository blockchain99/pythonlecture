import unittest
class SomeTests(unittest.TestCase):
    def testing_for_error(self):
        """testing for an error"""
        with self.assertRaises(IndexError):
            l = [1,2,3]
            # l[100] # ran OK
            l[1] # AssertionError: IndexError not raised
if __name__ == "__main__":
    unittest.main()