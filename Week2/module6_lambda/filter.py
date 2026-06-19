# even

a=[1,2,3,4]
even= list(filter(lambda x:x%2==0,a))
print(even)

# normal

a=[1,2,3,4]
nml= list(filter(lambda x:x,a))
print(nml)

# int or string

a=[1,"n",4,"ni"]
lst= list(filter(lambda a:isinstance (a,int), a))
print(lst)

# number greater than 10

a=[11,23,1,2,3,34,2]
g=list(filter(lambda x: x>10,a))
print(g)

# prime
def prime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c+=1
    return c==2
a=[5,4,3,45,32,2]
is_prime= list(filter(prime,a))
print(is_prime)
###is_prime= list(filter(prime(a),a))   prime(a) give error--- function object should be used 