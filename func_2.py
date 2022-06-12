'''

Function:

'''
'''
Basically there are 2 types of function:
1. Built in functions: the function provided by python itself
Example:
id()
print()
type()
round()
eval()
input()
etc
-----------------------------------------------------------
2. User defined functions:
User will design a function as per the requirements and need

While creating a function we have to do 2 things
a. declaration
def function_name():
    pass
    return value <optional>
    
b. calling
function_name()
----------------------------------------
- function can be empty
- we can pass arguments to a function its nothing but parameter

PARAMETER: are inputs to function. If a function contains parameters then at the time 
of calling compulsory you have to provide values.

def test(a,b):
    print(a+b)
test(20,2)


Otherwise u will get error.
def test(a,b):
    print(a+b)
test(20)
----------------------------------------
WAP to take a number from user and calculate square of it.

def square(n):
    print('Square of ',n, 'is',n**2)

n = int(input('Enter the number:'))
square(n)
----------------------------------------------------
WAP to calculate square of 1-10 numbers

def square(n):
    print('Square of ',n, 'is',n**2)

for i in range(1,11):
    square(i)
----------------------------------------------------
Que> What is call by ref and call by value?????
> what is difference between parameter and argument?
> How many times we can call function
> what is advantage of a function
> when to use a function
----------------------------------------------------------------
return statement:
function can return something as per the requirement
it is optional
but when we want to create a logic which is based on return of a function 
then use return statement
---------------------------------------------
def add(a,b):
    # print(a+b)
    total = a + b
    if total>25:
        return 'Its Good'
    else:
        return 'Its bad'
val = add(10,2)
# print(val)
if val == 'Its Good':
    print('Processing')
else:
    print('Stop processing')

------------------------------------------------
# Assignment: WA function to find out even and odd numbers with return statement
----------------------------------
We can return multiple values from a function
---------------------------------
def test(a,b):
    sum = a + b
    sub = a - b
    mult = a * b
    return sum,sub,mult
    # return must be inside a block

# it is packing of data
x = test(10,20)
print(x)
print(type(x))
print('------------Now unpack data-----------------')

x,y,z = test(10,20)
print(x)
print(y)
print(z)
--------------------------------------------------------
# Assignment: WA function to find out factorial of 1,6 numbers
'''


