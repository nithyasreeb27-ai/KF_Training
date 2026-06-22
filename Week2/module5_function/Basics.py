# No argument, No return

def func():
    print("hello")
func() #calls and execute function
print(func()) # func()-- prints hello and print expects return value & print them, else None will be printed

# Argument, no return

def func(a,b):
    print(a+b)
func(1,2)

# no argument, Return

def func():
    return 1
print(func())

# Argument, Return

def func(a,b):
    return (a+b)
print(func(1,2))

# Default parameter

#1
def func(a=8):
    print(a)
func(4)

#2
a=10
def func(a=[]):
    a.append(1)
    return a
print(func())
print(func())

