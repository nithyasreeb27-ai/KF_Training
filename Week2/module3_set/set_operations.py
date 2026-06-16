a={1,2,3,4}
b={3,4,5,6}

#UNION  (ALL, COMBINE, MERGE)
print(a|b)
print(a.union(b))

#INTERSECTION (COMMON, SHARED, BOTH, OVERLAP)
print(a&b)
print(a.intersection(b))

#DIFFERENCE (ONLY, EXCLUSIVE, PRESENT IN ONE AND NOT IN ANOTHER)
print(a-b)
print(b-a)
print(a.difference(b))

#SYMMETRIC DIFFERENCE (NOT COMMON FROM BOTH)
print(a^b)
print(a.symmetric_difference(b))

#SUBSET
print(a<=b)
print(a.issubset(b))

# SUPERSET
print(a>=b)
print(a.issuperset(b))

#DISJOINT (NO COMMON VALUES ,CHECKS AND RETURN TRUE OR FALSE)
print(a.isdisjoint(b))