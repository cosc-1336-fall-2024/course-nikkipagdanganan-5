import unittest

from src.examples.c_decisions.decisions import test_config, test_is_number_in_range

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_logical_and_truth_table(self):
        self.assertEqual(False, False and False)
        self.assertEqual(False, False and True)
        self.assertEqual(False, True and False)
        self.assertEqual(True, True and True)

    def test_logical_or_truth_table(self):
        self.assertEqual(False, False or False)
        self.assertEqual(True, False or True)
        self.assertEqual(True, True or False)
        self.assertEqual(True, True or True)

    def test_logical_not_truth_table(self):
        self.assertEqual(False, (not True))
        self.assertEqual(True, (not False))
        
    def test_and_with_only_one_false(self):
        self.assertEqual(False, True and True and True and True and False)

    def test_or_with_one_true(self):
        self.assertEqual(True, False or False or False or False or True)

    def test_logical_operators_order_of_precedence(self):
        self.assertEqual(True, not False and not False) #we infer that the "not" operator takes precedence over "and"
        self.assertEqual(True, True or True and False) #infer that "and" takes precedence over "or"
        self.assertEqual(True, not False and False or True)
        self.assertEqual(True, True and True or False)

    def test_if_a_number_is_in_a_range(self): 
        self.assertEqual(True, 1 >= 1 and 1 <= 10 ) #number in range 1 to 10 (exaple 1 is in range and 10 also)
        self.assertEqual(True, 10 >= 1 and 10 <= 10)
        self.assertEqual(True, 5 >= 1 and 5 <= 10)
        self.assertEqual(False, 0 >= 1 and 0 <= 10)
        self.assertEqual(False, 11 >= 1 and 11 <= 10)

    def test_is_number_in_range(self):
        self.assertEqual(True, is_number_in_range(1,10,1))
        self.assertEqual(True, is_number_in_range(1,10,10))
        self.assertEqual(True, is_number_in_range(1,10,5))
        self.assertEqual(False, is_number_in_range(1,10,0))
        self.assertEqual(False, is_number_in_range(1,10,11))
        self.assertEqual(False, is_number_in_range(1,10,100))