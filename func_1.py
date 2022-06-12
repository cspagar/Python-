'''
Function:
It is a single unit, where we can put statement/s
which we needed to execute multiple times

# older approach
# if i want python to be printed 4 times
print('python')
print('python')
print('python')
print('python')
print('----------------------------')
print('Python '*4)
print('----------------------------')
for i in range(4):
    print('Python')
-----------------------------------------------------------------------
# new approach
function approach is: write ones and use multiple times
Declare only ones + execute/call it multiple times

Advantage of a function:
Code reusability

-----------------------------------------------
Syntax:
Declaration + calling

def function_name():
    statement/s
    procedures

function_name()
----------------------------------------------------
# declaration
def addition():
    print('Addition is:', 40 + 60)

addition()
#calling

for i in range(10):
    print(i)

print(list(range(6)))

addition()
d = {1:200,2:300}
print(d)
addition()
addition()
addition()
addition()
--------------------------------------------------
'''
# lets supply some arguments to the function
def addition(x,y,z):
    print('Addition is:', x + y + z)
# number of arguments declared in function must match in calling
addition(1,2,1)
addition(10,20,2)
addition(-3,4,3)
