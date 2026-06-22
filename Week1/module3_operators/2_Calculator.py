n=int(input("enter number of values:"))
val=int(input("enter values:"))
for i in range(n-1):
    val2=int(input("enter value:"))
    exp=input("enter expression:")
    if(exp=="+"):
        new=(val+val2)
    elif(exp=="-"):
        new=(val-val2)
    elif(exp=="*"):
        new=(val*val2)
    elif(exp=="/"):
        new=(val/val2)
    elif(exp=="%"):
        new=(val%val2)
    elif(exp=="**"):
        new=(val**val2)
    val=new
    print(new)