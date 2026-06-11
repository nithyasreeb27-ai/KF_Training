# remove vowels

a=input("enter:")
vowels="aeiou"
new="" 
for i in a:
    if(i not in vowels):
        new+=i
print(new)