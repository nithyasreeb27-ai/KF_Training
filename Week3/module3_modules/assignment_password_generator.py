import random
import string
def requirements():
    # pattern1
    alp="abcdefghijklmnopqrstuvwxyz"
    num="1234567890"
    sym="!@#$%^&*~_"
    characters=alp+num+sym
    s=[]
    s.append(random.choice(string.ascii_lowercase))
    s.append(random.choice(string.ascii_uppercase))
    s.append(random.choice(string.digits))
    s.append(random.choice(string.punctuation))

    # pattern2
    '''characters=(string.ascii_letters+ string.digits+ string.punctuation)'''
    return s,characters

def generate_password(s,characters):

    #pattern1
    num=int(input("enter the password length:"))
    if num<=4:
        print("Length should be more than 4")
    else:
        a=random.choices(characters,k=num-4)
        a.extend(s)
        random.shuffle(a)
        password="".join(a)
        return password

    #pattern2
    '''s=""
    for i in range(8):
        a=random.choice(characters)
        s+=a
    return s'''

def main():
    s,characters=requirements()
    return generate_password(s,characters)

print(main())