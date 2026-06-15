s1=input("enter:")
s2=input("enter:")
if (len(s1)!=len(s2)):
    print("Not anagram")
else:
    for i in s1:
        if (s1.count(i)!=s2.count(i)):
            print("Not anagram")
            break
    else:
        print("anagram")