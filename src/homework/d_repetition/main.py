import repetition

def main():

    print( """
    Homework 3 Menu
    1-Factorial
    2-Sum odd numbers
    3-Exit
    """)

    menu = int (input ('Select action by entering number and press Enter. '))


    if menu == 1:
        prompt = int (input ('Enter a number to get its factorial: '))
        if prompt > 0 and prompt < 10:
            answer = repetition.get_factorial(prompt)
        print('The factorial of', prompt, 'is ', answer)
        exit = input('Enter EXIT if you want to exit. Press ENTER to continue.')
        if exit == 'EXIT' or exit == 'exit':
            print('Goodbye.')
        else:
            main()
        


    elif menu == 2:
        prompt = int (input ('Enter a number to get the sum of odd numbers within the number: '))
        if prompt > 0 and prompt < 100:
            answer = repetition.sum_odd_numbers(prompt)
        print('The sum of odd numbers within ', prompt, 'is ', answer)
        exit = input('Enter EXIT if you want to exit. Press ENTER to continue.')
        if exit == 'EXIT' or exit == 'exit':
            print('Goodbye.')
        else:
            repetition.main()

        

    elif menu == 3:
        prompt = input ('Would you like to continue using these tools? If so, enter Y. ')
        if prompt == 'Y' or prompt == 'y':
            main()
        else:
            print("Goodbye.")

    else:
        main()

    
main()