import unittest

from src.examples.h_strings.strings import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_string_concatenation(self):
        lang = 'Python'
        result = lang + ' is easy to learn'

        self.assertEqual('Python is easy to learn')

    def test_string_is_alphanum(self):
        str = 'Cpp'

        self.assertEqual(False, str.isalum())
        

