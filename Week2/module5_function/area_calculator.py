def triangle(b,h):
    return (b*h)/2
def rectangle(l,b):
    return (l*b)
def square(a):
    return (a*a)
def circle(r):
    return 3.14*r*r

# n=input("enter shape:")
# if(n.lower()=="triangle"):
#     b=int(input("enter value1:"))
#     h=int(input("enter value2:"))
#     print(triangle(b,h))
# elif(n.lower()=="rectangle"):
#     l=int(input("enter value1:"))
#     b=int(input("enter value2:"))
#     print(rectangle(l,b))
# elif(n.lower()=="square"):
#     a=int(input("enter value:"))
#     print(square(a))
# elif(n.lower()=="circle"):
#     a=int(input("enter value:"))
#     print(circle(a))




# ADVANCE
def calc(shapes,*args):
    if(shapes=="triangle"):
        return triangle(*args)

n=input("enter:")
shapes={
    "triangle":triangle,
    "rectangle":rectangle,
    "square":square,
    "circle":circle
}
# print(shapes[n](2))

