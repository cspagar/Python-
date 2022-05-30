'''
OOP: Object oriented programming
Everything in python is an object

What is object????
Is an entity exist in a memory
which has an id/address assigned

How object gets created??
==> it gets created using a class

what is class ??
class is template, its a blueprint, structure, plan, architecture

class in our case:
collection of 2 things
1. Properties: attributes, variables, identifiers
2. Behaviour: methods/functions
Example:
class Mobile:
    os
    RAM
    processor
    camera
    pixel
    color
    .
    .
    shutdown()
    powerOn()
    restart()
    reboot()
    backup()


class Human:
    properties:
                eyes
                hands
                legs
                ht
                wt
                color
                ......
    behaviour:operations/methods/function/processing
                talk()
                walk()
                speak()
                hear()
                run()
                sense()

print(id(23))
a = 23
print(id(a))
print(type(a))

How many objects we can create???
:- n no. of objects

How to check object size of object?
a = 78
# will tell u size in  bytes
print(a.__sizeof__())

---------------------------------------------------------------
Lets start with class and object
e307
---------------------------------
# there is no inherent limit for int value
#a = 23423555555555524234444444444444444444444444444444444444444423424242342342423423424234444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444442342342423442342
#print(a)
#for float we have limit of e^307
a  =2.0**10057
print(a)
-------------------------------------

# Class + object
# while writing a class follow CamelCase
class Sample:
    s1 = 20
    s2 = 'java'

    def method(self):
        print('This is my first method in class sample')

# Now we have just created structure of Sample

# in order to make it available in the memory we need to create an object
# to create an object we need a constructor
# what is constructor??
# constructor is nothing but calling of a class
# in current case: Sample() is a constructor
# why it is needed???
# it is need to allocate a memory
object1 = Sample()
print(object1.s1)
print(object1.s2)
object1.method()
# object1 is object of class Sample
# Sample() is a constructor
#--------------------------------------------
# if we are not creating an object, we don't have an access to members inside a class

s1
s2
method()

'''
class Car:
    wheels = 4
    color = 'red'

    def drive(self):
        print('Start Car and drive')

    def gear(self):
        print('Use gears to + - speed')
'''
print(Car().wheels)
print(Car().color)
print('----------------------------------')
bmw = Car()
print(bmw.wheels)
print(bmw.color)
--------------------------------------
print(id(Car().wheels))
print(id(Car().color))
print(id(Car().drive()))
print('--------Using Object----------')
bmw = Car()
print(id(bmw.wheels))
print(id(bmw.color))
print(id(bmw.drive()))
-----------------------------------

class Test:
    x =10
    y = 20

print(Test().x)
Test().x = 100
print(Test().x)
print(id(Test().x))
print('----------------------')
t = Test()
print(t.x)
print(id(t.x))
t.x = 100
print(t.x)
print(id(t.x))
'''
class Test:
    x = 40
    def m1(self):
        print('m1 of test')
t1 = Test()
t1.m1()

t2 = Test()
print(t2.x)

t3 = Test()
print(t3.x)
t3.m1()




