def dedupe(items):
    dupl=[]
    for item in items:
        if item not in dupl:
            dupl.append(item)
    return dupl
# items=[1, 2, 2, 3, 1]
items=list(map(int,input("enter numbers:").split()))
print(f"First seen order:{items}")
print(f"Deduplicated order:{dedupe(items)}")