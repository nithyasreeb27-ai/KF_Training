# pattern1

def triangle(b,h):
    return (b*h)/2
def rectangle(l,b):
    return (l*b)
def square(a):
    return (a*a)
def circle(r):
    return 3.14*r*r

def shapes(n):
    if(n.lower()=="triangle"):
        b=int(input("enter value1:"))
        h=int(input("enter value2:"))
        return triangle(b,h)
    elif(n.lower()=="rectangle"):
        l=int(input("enter value1:"))
        b=int(input("enter value2:"))
        return rectangle(l,b)
    elif(n.lower()=="square"):
        a=int(input("enter value:"))
        return square(a)
    elif(n.lower()=="circle"):
        a=int(input("enter value:"))
        return circle(a)


#pattern 2

def triangle(*args):
    b, h = args
    return (b * h) / 2

def rectangle(*args):
    l, b = args
    return l * b

def square(*args):
    a, = args
    return a * a

def circle(*args):
    r, = args
    return 3.14 * r * r


def shapes(shape, *args):

    if shape.lower() == "triangle":
        return triangle(*args)

    elif shape.lower() == "rectangle":
        return rectangle(*args)

    elif shape.lower() == "square":
        return square(*args)

    elif shape.lower() == "circle":
        return circle(*args)

    else:
        return "Invalid Shape"


shape = input("Enter Shape: ")

if shape.lower() in ("triangle", "rectangle"):
    v1 = float(input("Enter value 1: "))
    v2 = float(input("Enter value 2: "))
    print(shapes(shape, v1, v2))

elif shape.lower() in ("square", "circle"):
    v1 = float(input("Enter value: "))
    print(shapes(shape, v1))

else:
    print("Invalid Shape")

# # ADVANCE
# def calc(shapes,*args):
#     if(shapes=="triangle"):
#         return triangle(*args)

# n=input("enter:")
# shapes={
#     "triangle":triangle,
#     "rectangle":rectangle,
#     "square":square,
#     "circle":circle
# }

# # print(shapes[n](2))

