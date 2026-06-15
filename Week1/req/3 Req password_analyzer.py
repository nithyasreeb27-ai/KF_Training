a=input("enter password:")
l=len(a)
upper=0
spl_chr=0
dig=0
lower=0
if(l<8 and l>16):
    print("Invalid password, Password should contain 8 letters minimum")
else:
    for i in a:
        if(i.isupper()):
            upper+=1
        if(i.isdigit()):
            dig+=1
        if(i in "@$#%"):
            spl_chr+=1
        if(i.islower()):
            lower+=1
        if(i.isspace()):
            print("invalid")
            break
    has_upper=upper>0
    has_lower=lower>0
    has_digit=dig>0
    has_spl_chr=spl_chr>0

    category=(has_upper+
              has_lower+
              has_digit+
              has_spl_chr)
    print(category)
    if(category==4):
        print("strong password")
    elif(4>category>=2):
        print("medium password")
    elif(category<2):
        print("Weak password")