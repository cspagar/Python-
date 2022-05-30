'''
Types of variables:
local variable:
        the variable declared inside a class/method
        is a local variable
        & that var. is only accessible inside the class+ inside the method resp.
-----------------------------------------------------------
class Sample:
    x = 90 #local to class
    def test(self):
        a = 'py' #local to method
    print(a) #here we r trying to access a outside the block
print(x)#hre we r trying to access x outside the class
-------------------------------------------------------------------
class Sample:
    # variable declared inside a method is local variable
    def test(self):
        a = 'py' #pure local var. to method
        print(a) # inside a method , a will be accessible

s = Sample()
print(s.a) # outside class it wont be accessible
-----------------------------------------------------------------------------------
instance variable: if we want to access or modify local variables inside a class
+ outside a class too
static/class-level variable
class Sample:
    def add(self,a,b):
        print('a:',a)
        print('b:', b)
        print(a+b)
    def another(self):
        # in this way we cant access local variables of add into another
        # we need to make them instance
        print('a:', a)
        print('b:', b)
s = Sample()
s.add(20,30)
s.another()
print(s.a)
---------------------------------------------------------
# we can make local var. instance  using self keyword
class Sample:
    def add(self,a,b):
        #print(a+b)
        # lets make a and b as an instance
        self.a = a
        self.b = b
    def another(self):
        # in this way we cant access local variables of add into another
        # we need to make them instance
        print('lets print a and b')
        print(' Inside a:', self.a)
        print('Inside b:', self.b)
s = Sample()
s.add(20,30)
s.another()
print('Outside a:',s.a)
-------------------------------------------
Lets change the value of instance variable
class Sample:
    def m1(self,name):
        #p-rint(name)
        self.n = name
        # in above case self.n is instance and name is local
    def disp(self):
        print('Your name is:',self.n)
    def change(self):
        self.n = 'Java'
        print('After change, ur name is:', self.n)

s = Sample()
s.m1('Python')
s.disp()
s.change()
-------------------------------------------------------
Instance method: The method with self as ref. variable are instance method
Example:

def m1(self):
def add(self):

All default methods in python are instance
-----------------------------------------------------
class Sample:
    x = 1
    y = 2
    def t1(self):
        self.a = 'amit'
        self.b = 'baban'
    def t2(self):
        pass
        print('a from t2:',self.a)

# self: self in ref variable, it access everything inside a class
s = Sample()
s.t1()
print('a from t1:',s.a)
s.t2()
--------------------------------
instead of self we can use any variable
self acts same as that of this pointer in java
it points to current object: it access to each n everything present inside a class
-------------------------
class Sample:
    def m1(s):
        s.x = 800

    def m2(s):
        print(s.x)
------------------------------------------------------
Static var. :
the variable declared inside a class and outside a method

-[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[
class Sample:
    ifsc = 'SBI2343'
    # static or class level var.

    #lets access clas var. inside a method m1
    def m1(self):

        print('m1:',self.ifsc)
        print('m1 Sample:', Sample.ifsc)
        # self and Sample will work inside method only

    print(Sample.ifsc) # they wont work outside method
    print(self.ifsc)
    print('IFSC:',ifsc)

s = Sample()
print('object:',s.ifsc)
print('Clas:',Sample.ifsc)
s.m1()
--------------------------
class ATM:
    pin = 1234

    def m1(self):
        pass
        print(self.pin)
        print(ATM.pin)

a = ATM()
a.m1()
print(a.pin)
print(ATM.pin)
----------------------------------
'''










