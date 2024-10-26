import dictionary

def main():
    menu = int(input("""
    Welcome to p distance matrix program. Press 1 or 2 from the menu and hit Enter.
    1 - Get p distance matrix
    2 - Exit
    """))

    if menu == 1:
        list1 =  [ 
        ['T','T','T','C','C','A','T','T','T','A'],
        ['G','A','T','T','C','A','T','T','T','C'],
        ['T','T','T','C','C','A','T','T','T','T'],
        ['G','T','T','C','C','A','T','T','T','A'] 
        ]
        final = dictionary.get_p_distance_matrix(list1)
        print(final)
    elif menu == 2:
        print('Goodbye.')
    else:
        main()

main()