import unittest 
from stringCalculator import Add 

class TestStringCalculator(unittest.TestCase):

    #first test
    def test_first_test(self):
        self.assertTrue(True)

    #tests
    def test_fail_test(self):
        self.assertFalse(False)

    def test_empty_string(self):
        self.assertEqual(0, Add(""))

    def test_one_number(self):
        self.assertEqual(Add("1"), 1 )

    def test_two_numbers(self):
        self.assertEqual(Add("1,2"), 3)

    def test_several_numbers(self):
        self.assertEqual(Add("1,1,1,1,1"), 5)

    def test_new_line(self):
        self.assertEqual(Add("1\n2,3"), 6)

    def test_delimiter(self):
        self.assertEqual(Add("//;\n1;2"), 3)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            Add("1,-2,3")

    




