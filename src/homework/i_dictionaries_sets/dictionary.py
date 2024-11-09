def test_config():
    return True

inventory_dictionary = {}

def add_inventory(widget_name, quantity):  
    global inventory_dictionary

    if widget_name in inventory_dictionary:
        inventory_dictionary[widget_name] += quantity
        
    else:
        # widget_name = input('Enter widget name: ')
        # quantity = int (input('Enter widget quantity: '))
        inventory_dictionary = {widget_name : quantity}
    
    print(inventory_dictionary)

def remove_inventory(widget_name):
    global inventory_dictionary
    if widget_name in inventory_dictionary:
        del inventory_dictionary[widget_name]
        print(widget_name, ' deleted.')
    else:
        print('Item not found.')
    
    print(inventory_dictionary)