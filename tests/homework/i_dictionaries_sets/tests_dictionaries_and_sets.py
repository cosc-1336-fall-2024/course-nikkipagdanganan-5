import unittest


from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_add_inventory(self):
        inventory_dictionary = {}
        expected_inventory_dictionary = {'Widget1' : 10}

        widget_name = 'Widget1'
        quantity = 10

        if widget_name not in inventory_dictionary:
            inventory_dictionary[widget_name] = quantity

        self.assertEqual(inventory_dictionary, expected_inventory_dictionary)

        inventory_dictionary = {'Widget1' : 10}
        expected_inventory_dictionary = {'Widget1' : 35}

        widget_name = "Widget1"
        quantity = 25

        if widget_name in inventory_dictionary:
            inventory_dictionary[widget_name] += quantity

        self.assertEqual(inventory_dictionary, expected_inventory_dictionary)

        inventory_dictionary = {'Widget1' : 35}
        expected_inventory_dictionary = {'Widget1' : 25}

        widget_name = "Widget1"
        quantity = -10

        if widget_name in inventory_dictionary:
            inventory_dictionary[widget_name] += quantity

        self.assertEqual(inventory_dictionary, expected_inventory_dictionary)




#BELOW INSTRUCTIONS 1) CREATE DICT   2) ADD 2 WIDGETS   3) REMOVE WIDGET1   4) TEST LEN OF DICTIONARY AND WIDGET2 STILL THERE

    def test_remove_inventory_widget(self):
        inventory_dictionary = {}
        expected_inventory_dictionary = {'Widget1' : 10}
        widget_name = 'Widget1'
        quantity = 10

        if widget_name not in inventory_dictionary:
            inventory_dictionary[widget_name] = quantity

        self.assertEqual(inventory_dictionary, expected_inventory_dictionary)

#-----------TESTING SECOND PART OF QUESTION

        inventory_dictionary = {'Widget1' : 10}
        expected_inventory_dictionary = {'Widget1' : 10, 'Widget2' : 20}

        widget_name = 'Widget2'
        quantity = 20

        if widget_name not in inventory_dictionary:
            new_item = {widget_name : quantity}
            inventory_dictionary[widget_name] = 20

        self.assertEqual(inventory_dictionary, expected_inventory_dictionary)
    
#-----------TESTING LAST PART OF QUESTION
        inventory_dictionary = {'Widget1' : 10, 'Widget2' : 20}
        expected_inventory_dictionary = {'Widget2' : 20}

        widget_name = 'Widget1'

        if widget_name in inventory_dictionary:
            del inventory_dictionary['Widget1']

        self.assertEqual(1, len(inventory_dictionary))
        self.assertEqual(True, 'Widget2' in inventory_dictionary)

