a= input("enter:")
vowels="aeiou"
b=""
for i in a:
    if(i in vowels):
        b+="*"
    else:
        b+=i
print(b)