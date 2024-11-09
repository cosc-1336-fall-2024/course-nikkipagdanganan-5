import dictionary

def menu():
   print("""
Inventory Menu
1) Add or Update Item
2) Delete Item
3) Exit
""")

   selection = int(input('Make your selection and press enter. '))
   return selection

def main():
   while True:
      selection = menu()
      if selection == 1:
         wid = input('Enter a widget name: ')
         quant = int(input('Enter a widget quantity: '))
         dictionary.add_inventory(wid, quant)
      elif selection == 2:
         wid = input('Enter a widget name: ')
         dictionary.remove_inventory(wid)
      elif selection == 3:
         print('Goodbye.')
         break
      else:
         print('Select an option from the menu and press enter.')

main()