INTEREST_RATE = .059

#output comments variables input calculations output constants
def display_output():
    print('hello')

def test_config():
    return True

def float_division(value1, value2): #parameters(variables)
    return value1 / value2 #float division(decimals)

def integer_division(value1, value2):
    return value1 // value2

def use_named_constant():
    amount = 1000 * INTEREST_RATE
    print(amount)

def use_local_variables_int():
    num = 10
    print(num)
    print(num + 10)


def use_local_variables_str():
    num = '10'
    print(num)
    print(num + '10')


def use_reuse_local_variable():
    str1 = 'Python' #assign a value
    print(str1)

    str1 = 'C++' #reassign a value (see how str is same but value is different)
    print(str1)

def use_reuse_local_variable_data_type():
    num = 10 #whole number --- int
    print(num + 15)

    num = 10.99 #(float)
    print (num + .49)

    num = 'python' #string data type
    print(num)