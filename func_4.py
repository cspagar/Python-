'''
Higher order function:
Are those functions in which another function is used as an Input
1. Filter(func)
2. Map(func)
3. reduce(func)
-----------------------------------------------------------
Anonymous function: sometimes we want to declare a function without name
such type of function is anonymous function
or
we can call it as Nameless function

The purpose of this anonymous function is just for an instance use(for one time usage)
-----------------------------------
Lets compare normal function:
# WA function to square the number
def square(n):
    return n*n
print(square(4))
a = square(3)
print('Square is:', a)
-------------------------------------------
Lets see how we can do the same thing using lambda function
lambda parameter/s:expression
Note:
- we can use single/multiple parameters
- but only single expression

lambda n: n*n

--------------------------------------
s = lambda n:n*n
# print(s(10))
out = s(9)
print(out)
# lambda function has default return statement
-----------------------------------
# WA lambda function to do the addition of 2 numbers
add = lambda x,y: x +y
print('The addition is:',add(3,5))
print('The addition is:',add(30,50))
print('The addition is:',add(x=5,y=9))
----------------------------------------
Actual advantage is: it improves readablity of code
--------------------------------------------------
# WA lambda function to find out biggest number from 2 given numbers
def sssample():
    if a>b:
        return a
    else:
        return b
----------------------------------------
big = lambda a,b:a if a>b else b
a = 23
b = 12
print('Biggest number among',a,'&',b,'is:',big(a,b))
----------------------------------

check = lambda a: 'Even' if a%2==0 else 'Odd'

print(check(2))
-----------------------------------------
address = '7868273623'
func = lambda a : 'Enter 10 digit mobi.no' if len(a)!=10 else 'Correct mob. no.'
print(func(address))
----------------------------------------
# WAP to do the addition of variable length int numbers present in list
k1 = [1,2]
k2 = [3,4,5,6,9]
k3 = [100,200,300]

add = lambda a: sum(a)
# print(add(k2))
for i in [k1,k2,k3]:
    print(add(i))
-----------------------------------
'''
'''
1. Filter: it filter outs the values based on some conditions
Syntax: filter(func,sequence/iterable)


-------------------------------------------
# use normal function as an input
# fetch values divisible by 5 from sequence
k = [12,45,33,45,6,7,80,15,10,11]
def div(n):
    if n%5==0:
        return n

# print(div(10))#
# filter(function,iterable)

print(filter(div,k))
# whenever we get output in the form of object,
# then in order to get actual values from it we have 2 options
# 1. typecasting
# 2. perform iterations over it(use for or while loop)

print(list(filter(div,k)))
--------------------------------------

k = [12,45,33,45,6,7,80,15,10,11]
# five = lambda x:x%5==0
# print(list(filter(five,k)))
print(list(filter(lambda x:x%5==0,k)))
#here its nameless/anonymous
# filter is a creation of a new output/ sub sequence/sub-set
-------------------------------------------------------------------------------

f = ['amol','sheetal','sham']
# filter out the names those starts with s
# print(list(filter(lambda x:x.startswith('s'),f)))

for i in filter(lambda x:x.startswith('s'),f):
    print(i)
---------------------------------------------
map(): its a function, which wil be applied on each element from the sequence
Syntax: map(func,sequence/iterable)
-------
salary = [23000,45000,56000,21000]
#bonus = 5000
print(list(map(lambda x:(x+(x*.10)),salary)))
-------------------------------------------------
f = ['amol-patil','sheetal-pawar','sham-shinde']
#print(list(map(lambda n:n.upper(),f)))
#######################################
# print(list(map(lambda x:x.split('-'),f)))

print(list(map(lambda x:x.replace('-',' '),f)))
-----------------------------------------
reduce(): it reduces the sequence
it compacts the sequence into a single element
basically it is not present as a builtin 
so we have to import from functools module
--------------------------------------------------------
from functools import reduce
n = [200,23,45,67,55,67,89,100]

# do the addition of all elements
# print(sum(n))

# print(reduce(lambda x,y: x+y,n))

# find an average of numbers present in a list
# print(reduce(lambda x,y:(x+y),n)/len(n))
#print(sum(n)/7)

# lets find out biggest number from a sequence
print(reduce(lambda x,y: x if x>y else y,n))
--------------------------------------------------
what is filer map reduce?
what is difference between each?
Is there any similarity??
When to apply filter, map and reduce respectively???
---------------------------
Other than this:
decorator
iterator
generator
closure
------------------------------------------
from functools import reduce
n = [23,45,67,55,67,89,100]
print(reduce(max,n))
---------------------------------------
'''
from functools import reduce
n = [23,45,67,55,67,89,100]
output = reduce(max,n)













