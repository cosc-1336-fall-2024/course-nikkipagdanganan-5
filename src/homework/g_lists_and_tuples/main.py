import lists

def main():
    # show menu but keep input function collecting values
    # intake values for list, keep counter of how many values are entered
    # call both functions to have values stored
    menu = int (input ("""1. Show the list low/high values
2. Exit  """))
    listx = []
    if menu == 1:
        if len(listx) == 0:
            print('Need values to show the lowest/highest value.')
            addvals()
        else:
            print(f'The lowest value is {lists.get_lowest_list_values(listx)} \
                  and the highest value is {lists.get_highest_list_values(listx)}.')
    else:
        print('Goodbye.')

def addvals():
    counter = 0
    listx = []
    while counter < 3:
        vals = int(input ('Enter a value to the value list: '))
        listx.append(vals)
        counter += 1
    if counter >= 3:
        keepgoing = 'y'
        yesgo = input ('Do you want to enter another value? Y or N. ')
        if yesgo.lower() == 'n':
            keepgoing = 'n'
            print(f'The lowest value is {lists.get_lowest_list_values(listx)} and the highest value is {lists.get_highest_list_values(listx)}.')
        elif yesgo.lower() == 'y':
            while yesgo.lower() == 'y':
                addmore = int(input('Enter another value to the list: '))
                listx.append(addmore)
                yesgo = input ('Do you want to enter another value? Y or N. ')
                if yesgo.lower() == 'n':
                    yesgo == 'n'
                    print(f'The lowest value is {lists.get_lowest_list_values(listx)} and the highest value is {lists.get_highest_list_values(listx)}.')
                else:
                    print(f'The lowest value is {lists.get_lowest_list_values(listx)} and the highest value is {lists.get_highest_list_values(listx)}.')
        else:
            print(f'Neither Y or N was chosen. The lowest value is {lists.get_lowest_list_values(listx)} and the highest value is {lists.get_highest_list_values(listx)}.')

    return listx


main()