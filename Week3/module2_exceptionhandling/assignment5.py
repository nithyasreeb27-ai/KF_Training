class out_of_range(Exception):
    pass
try:
    marks=float(input("enter marks: "))
    if marks<0 or marks>100:
        raise out_of_range("The mark is out of range, it should be between 0 and 100")
    print("Mark:",marks)
except out_of_range as r:
    print(r)