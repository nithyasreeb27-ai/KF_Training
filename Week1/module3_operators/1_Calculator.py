a=int(input("enter 1st number:"))
b=int(input("enetr 2nd number:"))

print("""1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Exponential""")

c=int(input("enter the choice:"))
match c:
    case 1:
        print("The sum is:",a+b)
    case 2:
        print("The difference is:", a-b)
    case 3:
        print("The product is:",a*b)
    case 4:
        print("The answer is:",a/b)
    case 5:
        print("The remainder is:",a%b)
    case 6:
        print("The exponential value is:", a**b)
    case _:
        print("invalid")
