# friend1={"a","b","c","d"}
# friend2={"a","b","n","m"}
friend1= set((input("enter friends of friend1:").split()))
friend2= set((input("enter friends of friend2:").split()))
print(friend1)
print(friend2)
if(friend1.isdisjoint(friend2)==False):
    print("common friends: ", friend1&friend2)
else:
    print("No common friends")
print("all friends: ", friend1|friend2)
print("friends of friend 1 only: ", friend1-friend2)
print("friends of friend 2 only: ", friend2-friend1) 
print("Not common friends", friend1^friend2)
print("Does friend1 friends subset of friend2?", friend1.issubset(friend2))
print("Does friend1 friends superset of friend2?", friend1.issuperset(friend2))
# print("friend1 and friend2 have no common friends,", friend1.isdisjoint(friend2))