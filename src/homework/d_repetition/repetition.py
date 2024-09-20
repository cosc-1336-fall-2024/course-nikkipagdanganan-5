def test_config():
    return True




def get_factorial(num):
    
    fact = 1
    for i in range(1, num+1):
        fact *= i

    return fact 





def sum_odd_numbers(num):
    
    total = 0
    n = 1
    while n <= num:
        if n % 2 != 0:
            total += n
        n += 1

    return total



def exit():

    exit = input('Enter EXIT if you want to exit. Press ENTER to continue.')
    if exit == 'EXIT' or exit == 'exit':
        print('Goodbye.')
   
    main()
    


