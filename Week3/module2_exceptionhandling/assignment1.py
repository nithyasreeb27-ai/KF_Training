# Build a calculator that handles invalid input and division by zero.

def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    # try:
        return a/b
    # except ZeroDivisionError:
    #     print("Denominator shouldn't be zero")

def menu():
    print("""Menu:
1. add
2. sub
3. mul
4. div""")
    
    class choice_error(Exception):
        pass
    try:
        n=int(input("enter number:"))
        if 0>=n or n>=5:
            raise choice_error("the choice should be between 1 and 4")
            # print("invalid choice")
            # return
        a=int(input("enter 1st number:"))
        b=int(input("enter 2nd number:"))

        match n:
            case 1:
                return sum(a,b)
            case 2:
                return sub(a,b)
            case 3:
                return mul(a,b)
            case 4:
                return div(a,b)
    except choice_error as l:
        print(l)
    except ValueError:
        print("Enter correct value")
    except ZeroDivisionError:
        print("Denominator shouldn't be zero")
    except Exception:
        print("General error")
result=menu()
if result is not None:
    print(result())