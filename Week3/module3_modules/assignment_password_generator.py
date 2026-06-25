import random
import string
def requirements():
    # pattern1
    alp="abcdefghijklmnopqrstuvwxyz"
    num="1234567890"
    sym="!@#$%^&*~_"
    characters=alp+num+sym

    # pattern2
    '''characters=(string.ascii_letters+ string.digits+ string.punctuation)'''
    return characters

def generate_password(characters):

    #pattern1
    num=int(input("enter the password length:"))
    a=random.choices(characters,k=num)
    s="".join(a)
    return s

    #pattern2
    '''s=""
    for i in range(8):
        a=random.choice(characters)
        s+=a
    return s'''

def main():
    characters=requirements()
    return generate_password(characters)

print(main())