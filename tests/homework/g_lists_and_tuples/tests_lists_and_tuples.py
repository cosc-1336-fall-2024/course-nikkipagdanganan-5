import unittest

from src.homework.g_lists_and_tuples.lists import get_lowest_list_values, get_highest_list_values, test_config

class Test_config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    
    def test_get_lowest_list_value(self):
        self.assertEqual(1, get_lowest_list_values([ 8, 10, 1, 50, 20]))
        self.assertEqual(50, get_highest_list_values([ 8, 10, 1, 50, 20]))