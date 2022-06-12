'''
Types of arguments in a function:

def test(a,b):# formal arguments
    process
test(10,20) # actual arguments

There are total 4 types of Actual arguments:
1. positional argument:
In this case, position/sequence order matters
if we change the position then possession of values will change
----------------------------------
def sample(name,age):
    print('Your name is:',name,'your age is:', age)

sample(31,'Python')
# hence in case of positional arg. u must have to maintain sequence order
# no. of arg. must match, and its should be equal to no,.of parameters
---------------------------------------------
'''
'''
2. keyword arguments:
Here we dont have to worry abt sequence order
we can pass arg. values by keyword, it means by parameter name

def sample(name,age):
    print('Your name is:',name,'your age is:', age)

sample(age = 31,name = 'Python')
-----------------------------------------------
def bank(nm,ifcs,branch,location):
    print(nm,ifcs,branch,location)
# positional args.
# bank('SBI1345','Pune','SBI','Swargate')

#give keyword args
bank(ifcs='SBI1345',location='Pune',nm='SBI',branch= 'Swargate')
# format is : arg = value
--------------------------------------------
Suppose we are using combination of positional and keyword arg???
-----------------------------
def sample(name,age):
    print(name,age)

# sample('sham',name = 'amit') #will get error here

# sample('sham',age=22) # we wont get error

#sample(age = 22,'sham') #will create syntax error
# positional arguments must not follow keyword arguments
# Rule: if we r using combi. of positional + keyword arg,
# then keyword argument must be at the end
---------------------------------
3. Default arguments:
It is present in declaration
When we want to take some unique values which will work as a default, but we
have a privilage to change it further as per the need
Default arguemnt must be at the end.
----------------------------------------------
def operating_system(account='Guest'):
    print('Hello...Welcome', account)

operating_system()# whnen we r not supply it will take default Guest value
operating_system('Admin') #bt when we supply, it will take our given value
operating_system('Hacker')
operating_system()
-----------------------------------------
Suppose we want to combine Keyword and default
----------------------------------
def operating_system(account='Guest',x=10, y=10 ):
    print('Hello...Welcome', account)
    print(x,y)

operating_system(x = 200, y = 400)# whnen we r not supply it will take default Guest value
operating_system(account='Pythonist',x = 300,y =100,)
operating_system(x = 10,y = 20,account='Admin')
-----------------------------
4. Variable length argument:
When we have to supply variable no. of actual arguments
or
No. of actual arguemnts changes as per the requiremnt
sometime it may be 2/3/4/0
then we hv a below 2 options 
a. Variable length positional arguments
we can use *args/*any_identifier to make arguments as variable length
this argument returns ===> tuple of elements/empty tuple
What is *args??
-----------------------------------
# here * mean operator which makes n as variable length arg
def sample(*args):
    print(args)

sample(10)
sample(10,20)
sample(4,5,6,7)
sample()
----------------------------------

b. Variable length keyword arguments
we can use **kwargs/**any_identifier to make arguments as variable length

this argument returns ===> dict of elements/empty dict
What is **kwargs??
-------------------------------------------------
def details(default = '4444',**kwargs):
    # print(default)
    print(default,kwargs)

details(name = 'Amol',default='0000')
details(name = 'Omkar',age= 23)
details(place = 'Pune', pincode = 411047, dist = 'Pune')
details()
----------------------------------------------------
'''










