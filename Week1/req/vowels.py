a=input("enter:")
vowels="aeiou"
count=0
for i in a:
    if(i.lower() in vowels):
        count+=1
if count>0:
    print(count, "number of vowel present in this word")
else:
    print("no vowels present in the word")