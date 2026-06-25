import assignment_calculator

def display():
    print("Calculator")
    print("""MENU:
1. add
2.sub
3.mul
4.div""")
    
def input_values():
    a=int(input("Enter number1:"))
    b=int(input("Enter number2:"))
    exp=int(input("Enter Choice"))
    return exp,a,b

def calculate(exp,a,b):
    match exp:
        case 1:
            return assignment_calculator.add(a,b)
        case 2:
            return assignment_calculator.sub(a,b)
        case 3:
            return assignment_calculator.mul(a,b)
        case 4:
            try:
                return assignment_calculator.div(a,b)
            except ZeroDivisionError:
                return "b shouldn't be zero"
        case _:
            return "Invalid Choice"
def main():
    display()
    exp,a,b=input_values()
    return calculate(exp,a,b)

print(main())
