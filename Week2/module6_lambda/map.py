# Baisc map
n=[1,2,3]
txt=list(map(str,n))
print(txt)

# check vowel

text="apple"
is_vowel= map(lambda x: x in "aeiou",text)
lst=(list(is_vowel))
print(lst)
print(sum(lst))