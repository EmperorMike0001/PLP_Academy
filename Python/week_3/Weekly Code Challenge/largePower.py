'''Create a method that tests whether the result of taking the power of one number to another number provides an answer which is greater than 5000. 
We will use a conditional statement to return True if the 
result is greater than 5000 or return False if it is not. 
In order to accomplish this, we will need the following steps:

Define the function to accept two input parameters called base and exponent
Calculate the result of base to the power of exponent
Use an if statement to test if the result is greater than 5000. If it is then return True. Otherwise, return False'''


def LargePower(base , exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else :
        return False

try:
    base = int(input("enter the base number : "))
    exponent = int(input("enter the exponent number : "))
    print(LargePower(base , exponent))
except ValueError :
    print ("enter valid number ")


