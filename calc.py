import math
import os
# Calculator program
# Function for calculations
def calc():
    # Take input from the user.
    operation = input('''What operation do you want to perform?
        add = addition
        sub = subtraction
        mult = multiply
        div = division
        sqrt = Square root
        ''')
    if operation == 'sqrt':
        num1 = float(input('Please enter your number: '))
    else:
        num1 = float(input('Please enter your first number: '))
        num2 = float(input('Please enter your second number: '))
    # add
    if operation == 'add':
        result = (num1 + num2)
        print(num1, "+", num2, "=", result)
        return result
    # subtract
    elif operation == 'sub':
        result = (num1 - num2)
        print(num1, "-", num2, "=", result)
        return result
    # multiply
    elif operation == 'mult':
        result = (num1 * num2)
        print(num1, "*", num2, "=", result)
        return result
    # division
    elif operation == 'div':
        try:
            result = (num1 / num2)
            print(num1, "/", num2, "=", result)
            return result
        # can not divide by 0 error
        except ZeroDivisionError:
            print("Silly user, you can not divide by 0.")
    # square root
    elif operation == 'sqrt':
        try:
            result = math.sqrt(num1)
            print('The square root of', num1, 'is: ', result)
            return result
        # no imaginary numbers error
        except ValueError:
            print("Silly user, no imaginary numbers!")
    else:
        print('Invalid input. Please try again.')

#copy to clipboard
#print(result) - for testing before function was made
def addToClipBoard(result):
    command = 'echo ' + str(result) + '| clip'
    os.system(command)

# repeat the calc function if the user wants (decided by y or yes, any other input ends the program.)
again = 'y'
while again.lower() == 'y' or 'yes':
    result = calc()

    addToClipBoard(result)
    again = input('Would you like to do a calculation? ')
