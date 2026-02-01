#functions
'''
-it is a block of code that performs a specific task
-it will be executed only when it is called
-parameters and return values of a function will be decided based on the requirements
-it is a independent block of code
usages
- code optimization
- code reusability
- readability
Syntax:
def function_name(parameters):
    # logic
    return value/values #optional
---------------------------------------------------------------------
---------------------------------------------------------------------------------
calling a function
var_name=function_name(arguments) #optional arguments
res=add(a,b)
#then reuse the returned value
#---------------------------------------------------------
'''
#control flow of a function

# Example 1: Function with parameters and return value

# Called function
def addnum(n1, n2):      # function declaration with parameters
    sum = n1 + n2        # function definition (logic)
    return sum           # return value to the caller
    # Any statement after 'return' will not execute

# Function call
res = addnum(5, 3)       # 5,3 are arguments passed to function
print(res + 5)           # using returned value #8+5= 13
print(res - 5)           #8-5= 3
print(res * 10)
res2=addnum(10,20) 
print(res2)         #8*10= 80

# Notes:
# n1, n2 → parameters (local variables used inside function)
# 5, 3   → arguments (values passed to the function)
# return → gives output back to caller and ends function execution
#--------------------------------------------------------------------------------------------------------

# Example 2: Functions with and without return
def fun1():              # function without parameters, only prints
    a = 10
    b = 20
    product = a * b
    print(product)       # directly prints product, no return

def fun2(a, b):          # function with parameters and return
    product = a * b
    return product

# Multiple calls to fun1 (prints product each time)
fun1()#op- 200
fun1()#op- 200
fun1()#op- 200
print("-----------------------------------------------------------")

res = fun2(5, 8)
print("1st call =", res)#op= 40
res = fun2(10, 8)
print("2nd call =", res)#op= 80

'''

function declaration==>it icludes the basic details and requirement of the function
    a.function_name==>decided based on the task to be performed
    b.parameters==>the inputs required by a fun to perform a specific task
                    -they are dynamic local variables
                    
function definition==>
        -the logic associated to specific task
        -"return" ==>
                -basically a keyword
                -last executable line of code in a function
                - once "return " is executed in a function ,no other line of code ,included in the fun would woek
                    uses:
                        -it helps to return one or multiple values from  called function back to function call,that can be reused in further program
                        -it returns back the execution flow of pvm from called function back to function call              
'''
'''
steps to solve the problem using functions:
1)identify the major logic
2)include the function declaration and within it paste the major logic
3)analyse the I/P required by the function to start with logic
4)design the o/p statement
5)call the function by passing the value to the i/p parameter if any
6)reuse the o/p of the function by holding it in a variable if any
'''