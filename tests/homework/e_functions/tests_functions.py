import unittest

from src.homework.e_functions.value_return import get_hours, get_minutes, get_seconds, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_get_hours(self):
        self.assertEqual(1, get_hours(3800))
        self.assertEqual(1, get_hours(3800))

    def test_get_minutes(self):
        self.assertEqual(3, get_minutes(3800))
        self.assertEqual(0, get_minutes(3600))

    def test_get_seconds(self):
        self.assertEqual(20, get_seconds(3800))
        self.assertEqual(0, get_seconds(3600))

