import random
# random.seed(2)
print(random.random()) # No arguments
print(random.randint(1,11)) # 11 included
print(random.randint(1,100))
print(random.randrange(1,11)) # 11 not included
a=[1,2]
b="nithya"
print(random.choice(a))
print(random.choice(b))
print(len(dir(random)))
# random.shuffle(a)
print(a)
# random.shuffle(b) # As string is immutable throws error
