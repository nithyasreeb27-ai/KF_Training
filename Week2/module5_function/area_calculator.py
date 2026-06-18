def triangle(b,h):
    return (b*h)/2
def rectangle(l,b):
    return (l*b)
def square(a):
    return (a*a)
def circle(r):
    return 3.14*r*r

# def shapes(n):
#     if(n.lower()=="triangle"):
#         b=int(input("enter value1:"))
#         h=int(input("enter value2:"))
#         return triangle(b,h)
#     elif(n.lower()=="rectangle"):
#         l=int(input("enter value1:"))
#         b=int(input("enter value2:"))
#         return rectangle(l,b)
#     elif(n.lower()=="square"):
#         a=int(input("enter value:"))
#         return square(a)
#     elif(n.lower()=="circle"):
#         a=int(input("enter value:"))
#         return circle(a)


def triangle(*args):
    b, h= args
    return (b*h)/2
def rectangle(*args):
    l, b=args
    return (l*b)
def square(*args):
    a= args
    return (a*a)
def circle(*args):
    r=args
    return 3.14*r*r

def shapes(n,*args):
    if (n=="square"):
        return square(*args)
    elif (n=="triangle"):
        return triangle(*args)
    elif (n=="rectangle"):
        return rectangle(*args)
    if (n=="circle"):
        return circle(*args)
n=input("enter shape:")
print(shapes(n,4))


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

