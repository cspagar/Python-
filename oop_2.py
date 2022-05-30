'''
Class :
is a collection of Properties and behaviour
properties can be represented by variables/ attributes
behaviours can be implementd by Methods

Define???
class ClassName:
    """This is my first class"""
    variables: instance,static,local
    +
    methods: instance, class method,static method
-------------------------------------
class Cake:
    """
    This is class Cake
    """
#print(Cake.__doc__)
print(help(Cake))
print(help(int))
------------------------------------------------
Object:
Instance of a class==> that object will be present in a memory
# means exists Physically
Physical existence of a class is nothing but object
Syntax:
reference_variable = ClassName()

Example:
simple_cake = Cake()
sugar_free_cake = Cake()
ice_cake = Cake()
---------------------------------------------
REFERENCE VARIABLE:

The variable which can be used to refer object is called reference variable
Example:
class Cake:
    d = 87
c1 = Cake()
print(c1.d)
In above example d is reference variable

There is another reference variable: className
class Cake:
    d = 87
print(Cake.d)

in above example Cake which is class name , acts as a reference variable

Conclusion: Outside the class we have 2 ref. variables
1. object
2. className
---------------------------------------------------------
Another example:
class Cricket:
    team1 = 'IND'
    team2 = 'ENG'

# Access Team1 and 2 using reference var.
#1. using object
c1 = Cricket()
print(c1.team1)
print(c1.team2)
####################################
#2. Using className
print(Cricket.team1)
print(Cricket.team2)
---------------------------------------------------------
class Cricket:
    team1 = 'IND'
    team2 = 'ENG'

# Access Team1 and 2 using reference var.
#1. using object
c1 = Cricket()
print(c1.team1)
c1.team2 = 'AUS'
print(c1.team2)
c1.team2 = 'SA'
print(c1.team2)

print('##############using class Name######################')
#2. Using className
print(Cricket.team1)

#Cricket.team2 = 'NZ'
print(Cricket.team2)
print(c1.team2)
----------------------------------------------------------------
How to access members of a class???
using ref variable
object
className
---------------------------------
Lets add new members to a class
-------------------------------------
class Student:
    country = 'India'
    state = 'Maharashtra'


s1 = Student()
#s1.name = 'Amol'
#s1.age = 23

#print(list(s1))
#for i in s1:
#    print(i)
# These 2 methods fails in class case
# now if we want to see the output of  object s1
# use dir()
print(dir(s1))
s1.country = 'INDIA'
print(s1.__dict__) # this is dict representation of an object
print(s1.country)
print('--------------------------')

s2 = Student()
s2.name = 'Shital'
s2.place = 'Pune'
s2.salary = 34000
print(s2.__dict__)
'''
