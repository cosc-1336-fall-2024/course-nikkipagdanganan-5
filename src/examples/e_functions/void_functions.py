print(__name__)
import main
print('output', __name__)

#
GLOBAL_INT = 100

def hello_world():
    print("Hello World")
    print(GLOBAL_INT)


def display_number():
    num=5 
    print(num)
    print(GLOBAL_INT)


def show_numbers(num): #parameter - another name for a variable
    num1 = 5 #local variable 
    print("show_numbers", num, num1)
    print(GLOBAL_INT)


def local_and_params(num1):
    print("local_and_params0",num1)
    num1 = 10
    print("local_and_params1",num1)
    print(GLOBAL_INT)

def local_variable_scope():
    num = 5 # accessible in the local_variable_scope

    print(num)
    if(True):
        num1 = 1 # accessible outside of the if statement

    print(num1)

def local_variable_scope_1():
    num = 5
    print(num)

    while (num > 0):
        num1 = 1
        num -= 1

    print(num1)

def local_variable_scope_and_main():
    num = 5

    print(num)