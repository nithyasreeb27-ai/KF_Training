# ValueError
print(int("abc"))

# ZeroDivisionError
print(10/0)

# TypeError
print("10"+10)

# IndexError
a=[1,2]
print(a[10])

# try-except

try:
    a=int(input("enter:"))
    print(a)
except:
    print("Invalid input")

# try except important condition (try executes till the error and jumps to except)

try:
    a=int("123")
    print(a)
    b=int("abc")
    print(b)
except:
    print("c")

# Catching specific exception only

try:
    #10+"10"
    a=int("abc")
    print(a)
    10+"10"
except ValueError:
    print("Value error")
except:
    print("some error")

# using exception object:

try:
    a=int("abc")
    print(a)
    10+"10"
except ValueError as e:
    print(e)

# Multiple Exception

try:
    a=int(input("enter:"))
    b=int(input("enter:"))
    print(a/b)
except ValueError:
    print("Enter numbers only")
except ZeroDivisionError:
    print("Denominator shouldn't be zero")

# Multiple Exceptions Together

try:
    a=int(input("enter:"))
    b=int(input("enter:"))
    print(a/b)
except (ValueError,ZeroDivisionError):
    print("Invalid")

# With else

try:
    a=10
    b=2

    print(a/b)

except ZeroDivisionError:
    print("Error")

# with finally

try:
    print(10/0)

except ZeroDivisionError:
    print("Error")

finally:
    print("Always Runs")

# #pattern 2: (When error occurs,program stops, file ll bremain open, here finally helps to close the file)

'''file = open("data.txt")
try:
    data = file.read()
finally:
    file.close()
else:
    print("Success")'''


#  Raise with existing error

a=int(input("enter:"))
if a<0 or a>100:
    raise ValueError("Number range should be within 0 and 100") #If error occurs, stops execution
print("done") 

# Raise with try

try:
    marks = int(input())

    if marks > 100:
        raise ValueError("Marks too high")

except ValueError as e:
    print(e)

# Custom Exception
# Pattern 1
class InvalidMarksError(Exception):
    pass
marks = int(input("enetr:"))
if marks > 100:
    raise InvalidMarksError("Marks must be 0-100")

# Pattern 2
class InvalidMarksError(Exception):
    pass

try:
    marks = int(input("Enter Marks: "))
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks should be between 0 and 100") #This raises the error and crashes if left with except block
    print("Valid Marks")
except InvalidMarksError as e: # the error searches for except block, then the exception is assigned to exception object so we can use them for printing, PROGRAM doesn't crash)
    print(e)

# Error inside error

try:
    a=10/0
except ZeroDivisionError:
    print("Error")
try:
    print(a)
except NameError:
    print("Local error")