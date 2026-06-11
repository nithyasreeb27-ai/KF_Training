# Count of vowels

a=input("enter:")
vowels="aeiou"
count=0
for i in a.lower():
    if(i in vowels):
        count+=1
print("number of vowels present is", count)