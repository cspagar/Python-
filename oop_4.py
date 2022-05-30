'''
Variables: Local, instance, static/class level
Methods: instance,class method, static method
----------------------------------------------------
Constructor:
It is used to allocate a memory
or
it initializes member of class and make them available outside the class

Features of constructor:
Constructor has same name as that of class name
We can create/call constructor multiple times
class Sample:
    f = 67
    def m1(self):
        pass
Sample()
-----------------------------------------------------------------
Using constructor we can build an object

s = Sample()
-----------------------------------------------------------
If we want to write a method of a constructor then use def __init__(self): method
----------------------------------------------------
class Sample:
    def __init__(self):
        print('This is init...')

# Constructor calling means __init__ calling
Sample()
Sample()
------------------------------------------------
Lets use instance variables in init
--------------------------------------------
class Bank:
    def __init__(self):
        self.branch = 'Pune'
        self.ifsc = 'SBI7523'
        self.micr = 12324

    def display(self):
        #print('Branch is:{} IFSC is:{},MICR is:{}'.format(self.branch,self.ifsc,self.micr))
        print('Branch is:%s IFSC is:%s,MICR is:%d'%(self.branch,self.ifsc,self.micr))
        # % is format specifier
b = Bank()
b.display()
------------------------------------------
If i want to supply member through instance method __init__
----------------------------------------------------------------
class Bank:
    def __init__(self,b,i,m):
        self.branch = b
        self.ifsc = i
        self.micr = m

    def display(self):
        #print('Branch is:{} IFSC is:{},MICR is:{}'.format(self.branch,self.ifsc,self.micr))
        print('Branch is:%s IFSC is:%s,MICR is:%d'%(self.branch,self.ifsc,self.micr))
        # % is format specifier
"""
b = Bank('Kop','BOI2345',98793)
b.display()

b1 = Bank('Pune','BOM34345',567567)
b1.display()
"""
# ask user to supply the values
br = input('Enter the Branch:')
ifs = input('Enter the IFSC:')
mi = input('Enter the MICR:')
b = Bank(br,ifs,int(mi))
b.display()
-------------------------------------------------------
class Bank:
    def __init__(self,nm):
        self.nm = nm
        print('Name:',self.nm)
        print('We can change value of instance variable')
        #chagge nm
        self.nm = 'BOI'
        print('changed Name:', self.nm)

b = Bank('SBI')
print(b.nm)
----------------------------------------------------
To pass values, only constructor is not an option
 we can do the same thing using instance method also
---------------------------------------
class Student:
    def display(self,nm,age,place='Pune'):
        self.nm = nm
        self.age= age
        print(self.nm,self.age,place)

s = Student()
s.display('Amol', 30)

s1 = Student()
s1.display('Janvi',34,'Satara')
--------------------------------------------------------------
Class Method:
Q. What is class method? why we need???? when to use?? How its different from others/??

A method which is used to access class level or static variables is known as  class method

in order to create a class method we need @classmethod decorator
and instead of self we use cls as a reference variable
-------------------------------------
class Test:
    x = 66 #static or class level vr.

    @classmethod
    def catch(cls):
        print(cls.x)

t =  Test()
t.catch()

# Assignment: What is difference btwn instance and class method???
----------------------------------------------------
Static method:
A method which contains static variables and decorated with @staticmethod decorator
is known as static method.

which we can not access in any other method???or member of that method cannot be accessible
to any other

When we need static method????
When we want to perform operations only once,
or we dont want to change the supplied values

In this case we don't require self
'''
class Test:
    @staticmethod
    def m1(a,b):
        print(a+b)

t = Test()
t.m1(20,40)

